# Importing the Streamlit package which is used to create web applications
import streamlit as st

# Defining the main function for the application
def app():
    # Setting the title of the page
    st.title('User Persona')

    # Creating a form to input user persona information
    with st.form(key='user_persona_form'):
        # Text input field for the name of the persona
        name = st.text_input("Name der Persona")

        # Slider for selecting the age of the persona, with minimum 18, maximum 100, and default value 30
        alter = st.slider("Alter", 18, 100, 30)

        # Dropdown menu to select the gender of the persona
        geschlecht = st.selectbox("Geschlecht", ["Männlich", "Weiblich", "Andere"])

        # Text area for entering interests and hobbies of the persona
        interessen = st.text_area("Interessen und Hobbys")

        # Text area for entering values and attitudes of the persona
        werte = st.text_area("Werte und Einstellungen")

        # Text area for entering shopping habits of the persona
        einkaufsgewohnheiten = st.text_area("Einkaufsgewohnheiten")

        # Text area for entering social media usage of the persona
        nutzung_sozialer_medien = st.text_area("Nutzung Sozialer Medien")

        # Text area for entering brand preferences of the persona
        markenpraferenzen = st.text_area("Markenpräferenzen")

        # Button to submit the form
        submit_button = st.form_submit_button("User Persona erstellen")

        # Check if the submit button was pressed
        if submit_button:
            # Save the persona data in the session state
            st.session_state['persona_data'] = {
                "name": name,
                "alter": alter,
                "geschlecht": geschlecht,
                "interessen": interessen,
                "werte": werte,
                "einkaufsgewohnheiten": einkaufsgewohnheiten,
                "nutzung_sozialer_medien": nutzung_sozialer_medien,
                "markenpraferenzen": markenpraferenzen
            }

            # Display a success message
            st.success("User Persona erfolgreich erstellt!")

# This part is for testing purposes if you run this script directly
if __name__ == "__main__":
    app()
