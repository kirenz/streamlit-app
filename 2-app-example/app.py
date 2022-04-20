# SETUP

import streamlit as st
import numpy as np
import pandas as pd
from pickle import APPEND
from turtle import width

#-------------------
# CREATE DATA

# Simple dataframe
df = pd.DataFrame({
    'A': [1, 4, 3, 2],
    'B': [10, 20, 30, 40]
    })

#-------------------
# START OF APP

#-------------------
# HEADER

# Title of our app
st.title("Hello World!")
# Add header
st.header("This is my first app")
# Add a gif
st.markdown("![Alt Text](https://media.giphy.com/media/MeJgB3yMMwIaHmKD4z/giphy.gif)")

#-------------------
# BODY

#-------------------
# Show static DataFrame
st.subheader("Show Dataframe")
st.write("Here's our first attempt at using data to create a table:")
st.write(df)

#-------------------
# Highlight some attributes
st.write("DataFrame with highlight_max:")
st.dataframe(df.style.highlight_max(axis=0))

#-------------------
# Bar chart
st.subheader("Bar chart")
# standard bar chart
st.bar_chart(df)

#-------------------
# Show metric
st.subheader("Display Metrics")
st.metric("My metrics", 32, 4)

#-------------------
# Add slider with user input
st.subheader("Slider")
st.write("This is a Slider")
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

#-------------------
# Show code
st.subheader("Show some code")

code = '''def hello():
     print("Hello, Streamlit!")'''

st.code(code, language='python')