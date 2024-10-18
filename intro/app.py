# -------------------#
# EINRICHTUNG
import streamlit as st
import pandas as pd
import altair as alt
from pathlib import Path

# -------------------#
# PFADE VORBEREITEN

# Ermittle das Verzeichnis des aktuellen Skripts
script_dir = Path(__file__).parent

# Konstruiere den Pfad zur CSV-Datei
data_path = script_dir.joinpath("data", "oecd.csv") 
# Konstruiere den Pfad zur Bilddatei
image_path = script_dir.joinpath("img", "hdm-logo.jpg") 

# -------------------#
# DATEN IMPORTIEREN

df = pd.read_csv(data_path)


### -------------------###
# START UNSERER APP

# -------------------#
# KOPFZEILE

# Titel unserer App
st.title("Hallo Welt")


# Füge Bild hinzu (wir verwenden str (String), um den Bildpfad in einen String umzuwandeln)
st.image(str(image_path))

# Füge Überschrift hinzu
st.header("Mein Text")

# -------------------#
# SEITENLEISTE

# Überschrift
st.sidebar.header("Dies ist meine Seitenleiste")

# Erstelle einen Schieberegler
zufriedenheit = st.sidebar.slider('Wie zufrieden sind Sie mit Ihrem Leben?', 0, 10, 1)

# Zeige die Ausgabe der Schiebereglerauswahl an
st.sidebar.write("Meine Lebenszufriedenheit liegt bei etwa ", zufriedenheit, 'Punkten')

# -------------------#
# HAUPTTEIL

st.write("Schauen Sie sich meine Daten an")
# Zeige statischen DataFrame an
st.dataframe(df)

st.write("Schauen Sie sich mein Diagramm an")
# Erstelle ein Diagramm mit Altair

c = alt.Chart(df).mark_circle().encode(
    x='life_satisfaction',
    y='gdp_per_capita',
    color='country'
)

# Zeige Diagramm an
st.altair_chart(c, use_container_width=True)

### -------------------###
# ENDE DER APP