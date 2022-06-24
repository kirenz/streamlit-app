# SETUP


import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import datetime as dt
from datetime import datetime

#-------------------
# DATA

# Define path to data

home_path = str(Path.home())

# Import
df = pd.read_csv(home_path + "streamlit-app/data/covid.csv")

# Transformation
df['Date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')

#-------------------
# START OF APP

#-------------------
# HEADER

# Title of our app
st.title("Hello world!")
# Add header
st.header("This is my interactive app")

#-------------------
# BODY

#-------------------
# Show static DataFrame
st.subheader("Show Data")
st.write("Here's my data:")
st.dataframe(df)

#-------------------
# Show a map
st.write("Plot a map")
st.map(df)

#-------------------
# 


# Filters UI
subset_data = df
country_name_input = st.sidebar.multiselect(
'Country name',
df.groupby('Country/Region').count().reset_index()['Country/Region'].tolist())
# by country name
if len(country_name_input) > 0:
    subset_data = df[df['Country/Region'].isin(country_name_input)]