# SETUP

import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

#-------------------
#-------------------#
# IMPORT DATA

df = pd.read_csv("https://raw.githubusercontent.com/kirenz/datasets/master/oecd-new.csv")


# Data preparation
df = df.sort_values(by=['gdp_per_capita'], ascending=False)

###-------------------###
# START OF OUR APP

#-------------------#
# HEADER

# Title of our app
st.title("Hello World!")
# Add a gif
st.markdown("![Alt Text](https://media.giphy.com/media/MeJgB3yMMwIaHmKD4z/giphy.gif)")

#-------------------#
# BODY

# Show df and highlight some attributes
st.write("DataFrame with highlight_max:")
st.dataframe(df.style.highlight_max(axis=0))


# Bar chart
st.subheader("Bar chart")

c = alt.Chart(df).mark_bar().encode(
    x='country',
    y='life_satisfaction',
    tooltip = ['country', "life_satisfaction"]
)

st.altair_chart(c, use_container_width=True)

# Show metric
st.subheader("Display Metrics")
st.metric("My metrics", 32, 4)

# Add slider with user input
st.subheader("Slider")
st.write("This is a Slider")
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

# Show code
st.subheader("Show some code")

code = '''def hello():
     print("Hello, Streamlit!")'''

st.code(code, language='python')