# SETUP

import streamlit as st
import numpy as np
import pandas as pd
import altair as alt


#-------------------
# DATA

df = pd.read_csv("https://raw.githubusercontent.com/kirenz/datasets/master/housing_hml3.csv")


#-------------------
# START OF APP

#-------------------
# HEADER

# Title of our app
st.title("Hello world!")
# Add header
st.header("This is my app")
# Add a gif
st.markdown("![Alt Text](https://media.giphy.com/media/QpVUMRUJGokfqXyfa1/giphy.gif)")


#-------------------
# BODY

#-------------------
# Show static DataFrame
st.subheader("Show Data")
st.write("Here's my housing data:")
st.dataframe(df)

#-------------------
# Show a map
st.write("Plot a map of our districts")
st.map(df)

#-------------------
# Show a plot with Altair
st.subheader("Data exploration")

st.write("Scatterplot")

c = alt.Chart(df).mark_point().encode(
    x='median_income:Q',
    y='median_house_value:Q',
    color='ocean_proximity:N',
    tooltip=['median_income', 'median_house_value', 'ocean_proximity']
)

st.altair_chart(c, use_container_width=True)