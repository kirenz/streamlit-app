# SETUP
import streamlit as st

import numpy as np
import pandas as pd
import altair as alt

from pathlib import Path
import datetime as dt
from datetime import datetime

#-------------------
# DATA

# Obtain home path
home_path = str(Path.home())

# Data import
df = pd.read_csv(home_path + "/streamlit-app/data/covid.csv")

# Data transformation
df['Date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')



#-------------------
# START OF APP

#-------------------
# SIDEBAR

# Make a country list
country_list = st.sidebar.multiselect('Select country', df['country'].unique().tolist())

# Create a subset out of country_list 
if len(country_list) > 0:
    df_subset = df[df['country'].isin(country_list)]

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
st.dataframe(df_subset)

#-------------------
# Show a map
st.write("Plot a map")
st.map(df_subset)

#-------------------
