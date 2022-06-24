#-------------------#
# SETUP
import streamlit as st

import pandas as pd
import altair as alt

import datetime
from pathlib import Path

#-------------------#
# IMPORT LOCAL DATA

# Obtain home path
home_path = str(Path.home())
# Data import
df = pd.read_csv(home_path + "/streamlit-app/data/oecd.csv")

###-------------------###
# START OF APP

#-------------------#
# HEADER

# Title of our app
st.title("My first App")

# Image
st.image('hdm-logo.jpg')

# Add header
st.header("My header")

#-------------------#
# BODY

#-------------------
# Show static DataFrame

st.write("Take a look at my data")

st.dataframe(df)

#-------------------
# Make a chart with altair

st.write("Take a look at my chart")

c = alt.Chart(df).mark_circle().encode(
     x='life_satisfaction', 
     y='gdp_per_capita', 
     color='country',
     tooltip = ['life_satisfaction', 'gdp_per_capita', 'country']
     )

st.altair_chart(c, use_container_width=True)

#-------------------#
# SIDEBAR

# Header
st.sidebar.header("This is my sidebar")

# Slider
satisfaction = st.sidebar.slider('What is your life satisfaction?', 0, 10, 1)

st.sidebar.write("My life satisfaction is around ", satisfaction, 'points')

# Date
d = st.sidebar.date_input(
     "When's your birthday",
     datetime.date(2019, 7, 6))

st.sidebar.write('Your birthday is:', d)

###-------------------###
# END OF APP