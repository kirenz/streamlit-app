# SETUP

import streamlit as st
import pandas as pd
import datetime
from pathlib import Path


#-------------------
# IMPORT LOCAL DATA

# Obtain home path
home_path = str(Path.home())
# Data import
df = pd.read_csv(home_path + "/streamlit-app/data/oecd.csv")

#-------------------
#-------------------
# START OF APP

#-------------------#
# HEADER

# Title of our app
st.title("Meine erste App")
# Add header
st.header("Mein Header")
# Add a gif from https://giphy.com/
#st.markdown("![Katze](https://media.giphy.com/media/ICOgUNjpvO0PC/giphy.gif)")

#st.image('hdm-logo.jpg')

#-------------------#
# BODY


#-------------------
# Show static DataFrame
st.dataframe(df)

#-------------------
# Bar chart
st.bar_chart(df)

#-------------------#
# SIDEBAR

# Radio
st.sidebar.radio(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Slider
age = st.sidebar.slider('How old are you?', 0, 130, 25)
st.sidebar.write("I'm ", age, 'years old')

# Date
d = st.sidebar.date_input(
     "When's your birthday",
     datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)