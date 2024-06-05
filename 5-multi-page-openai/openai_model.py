 # Importing required packages
import streamlit as st
import openai
import uuid
import time
from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
from assistant import OPENAI_ASSISTANT


def app():
    st.title('OpenAI Model')

    # Initialize OpenAI client
    client = OpenAI()


    # Initialize session state variables
    if "session_id" not in st.session_state:
        st.session_state.session_id = str(uuid.uuid4())

    if "run" not in st.session_state:
        st.session_state.run = {"status": None}

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "retry_error" not in st.session_state:
        st.session_state.retry_error = 0


# Initialize OpenAI assistant
    if "assistant" not in st.session_state:
        openai.api_key = os.getenv('OPENAI_API_KEY')
        st.session_state.assistant = openai.beta.assistants.retrieve(OPENAI_ASSISTANT)
        st.session_state.thread = client.beta.threads.create(
            metadata={'session_id': st.session_state.session_id}
     )

# Display chat messages
    elif hasattr(st.session_state.run, 'status') and st.session_state.run.status == "completed":
        st.session_state.messages = client.beta.threads.messages.list(
            thread_id=st.session_state.thread.id
     )
        for message in reversed(st.session_state.messages.data):
            if message.role in ["user", "assistant"]:
                with st.chat_message(message.role):
                    for content_part in message.content:
                        message_text = content_part.text.value
                        st.markdown(message_text)


# Vorbereiten des initialen Prompts
    if 'persona_data' in st.session_state and 'company_data' in st.session_state:
        persona_data = st.session_state['persona_data']
        company_data = st.session_state['company_data']

    # Konvertieren der Daten in einen lesbaren String
        persona_str = ", ".join([f"{key}: {value}" for key, value in persona_data.items()])
        company_str = ", ".join([f"{key}: {value}" for key, value in company_data.items()])

        initial_prompt = f"Erstelle Werbetext basierend auf der User Persona ({persona_str}) und Unternehmensdaten ({company_str})."
    else:
         initial_prompt = "Bitte geben Sie Informationen zur User Persona und zum Unternehmen ein."

# Anzeigen des initialen Prompts
    st.text_area("Initialer Prompt (kopieren und bei Bedarf bearbeiten):", initial_prompt, height=100)


# Chat input and message creation with file ID
    if prompt := st.chat_input("Wie kann ich Ihnen helfen?"):
        with st.chat_message('user'):
            st.write(prompt)

        message_data = {
            "thread_id": st.session_state.thread.id,
            "role": "user",
            "content": prompt
        }

    # Include file ID in the request if available
        if "file_id" in st.session_state:
            message_data["file_ids"] = [st.session_state.file_id]

        st.session_state.messages = client.beta.threads.messages.create(**message_data)

        st.session_state.run = client.beta.threads.runs.create(
            thread_id=st.session_state.thread.id,
         assistant_id=st.session_state.assistant.id,
        )
        if st.session_state.retry_error < 3:
            time.sleep(1)
            st.rerun()

# Handle run status
    if hasattr(st.session_state.run, 'status'):
        if st.session_state.run.status == "running":
            placeholder = st.empty()
            with placeholder.container():
                with st.chat_message('assistant'):
                    st.write("Thinking ......")

        elif st.session_state.run.status == "failed":
            st.session_state.retry_error += 1
            with st.chat_message('assistant'):
                if st.session_state.retry_error < 3:
                    st.write("Run failed, retrying ......")
                    time.sleep(3)
                    st.rerun()
                else:
                    st.error("FAILED: The OpenAI API is currently processing too many requests. Please try again later ......")

        elif st.session_state.run.status != "completed":
            st.session_state.run = client.beta.threads.runs.retrieve(
                thread_id=st.session_state.thread.id,
                run_id=st.session_state.run.id,
         )
            if st.session_state.retry_error < 3:
                time.sleep(3)
                st.rerun()


if __name__ == "__main__":
    app()