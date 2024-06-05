# page_four.py

import streamlit as st

def app():
    st.title('Datenübersicht')

    # Check if persona_data is available in session state
    if 'persona_data' in st.session_state:
        persona_data = st.session_state['persona_data']

        # Format persona data as a plain text string
        persona_data_txt = "\n".join([f"{key}: {value}" for key, value in persona_data.items()])

        # Display persona data using markdown for better readability
        st.markdown(f"```\n{persona_data_txt}\n```")

        # Create a button to download the persona data as a .txt file
        st.download_button(
            label="Download Persona Data",
            data=persona_data_txt,
            file_name='persona_data.txt',
            mime='text/plain',
        )
    else:
        st.warning("No persona data found. Please create a user persona on 'Page One' first.")
