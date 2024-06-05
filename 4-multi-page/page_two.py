# company_info

import streamlit as st


def app():
    st.title('Unternehmensdaten')

    # Eingabefelder für Unternehmensdaten
    with st.form(key='company_info_form'):
        unternehmensname = st.text_input("Unternehmensname")
        branche = st.text_input("Branche")
        groesse = st.selectbox("Unternehmensgröße", ["Kleinunternehmen", "Mittelständisch", "Großunternehmen"])

        # Informationen zu USPs und Zielen
        usps = st.text_area("USPs (Unique Selling Points)")
        ziele = st.text_area("Zielsetzungen der Kampagne")

        # Informationen zur Markenpersönlichkeit
        markenpersoenlichkeit = st.text_area("Markenpersönlichkeit und -werte")

        # Informationen zu Hauptzielgruppen
        hauptzielgruppen = st.text_area("Hauptzielgruppen des Unternehmens")

        # Knopf zum Absenden des Formulars
        submit_button = st.form_submit_button("Unternehmensdaten speichern")

        if submit_button:
            # Speichern der Unternehmensdaten im session_state
            st.session_state['company_data'] = {
                "unternehmensname": unternehmensname,
                "branche": branche,
                "groesse": groesse,
                "usps": usps,
                "ziele": ziele,
                "markenpersoenlichkeit": markenpersoenlichkeit,
                "hauptzielgruppen": hauptzielgruppen
            }

            st.success("Unternehmensdaten erfolgreich gespeichert!")

if __name__ == "__main__":
    app()
