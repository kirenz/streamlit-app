# user_persona.py
import streamlit as st

def app():
    st.title('User Persona Creation')

    # Eingabefelder für grundlegende Informationen der User Persona
    with st.form(key='user_persona_form'):
        name = st.text_input("Name der Persona")
        alter = st.slider("Alter", 18, 100, 30)  # Min, Max, Default
        geschlecht = st.selectbox("Geschlecht", ["Männlich", "Weiblich", "Andere"])

        # Psychografische Daten
        interessen = st.text_area("Interessen und Hobbys")
        werte = st.text_area("Werte und Einstellungen")

        # Verhaltensdaten
        einkaufsgewohnheiten = st.text_area("Einkaufsgewohnheiten")
        nutzung_sozialer_medien = st.text_area("Nutzung Sozialer Medien")
        markenpraferenzen = st.text_area("Markenpräferenzen")

        # Knopf zum Absenden des Formulars
        submit_button = st.form_submit_button("User Persona erstellen")

        if submit_button:
            # Speichern der Persona-Daten im session_state
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

            st.success("User Persona erfolgreich erstellt!")

# Dieser Teil ist für Testzwecke, wenn Sie dieses Skript einzeln laufen lassen.
if __name__ == "__main__":
    app()
