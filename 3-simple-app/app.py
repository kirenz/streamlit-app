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
st.header("This is my interactive app")
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
    color='ocean_proximity:N'
)

st.altair_chart(c, use_container_width=True)

#-------------------
# Interactive plot with Altair

st.write("Interactive Scatterplot")


column_filter= df.filter().columns.tolist()

c = alt.Chart(df).mark_point().encode(
    x='median_income:Q',
    y='median_house_value:Q',
    color='ocean_proximity:N'
)

st.altair_chart(c, use_container_width=True)


# Filters UI
subset_data = df
country_name_input = st.sidebar.multiselect(
'Country name',
df.groupby('Country/Region').count().reset_index()['Country/Region'].tolist())
# by country name
if len(country_name_input) > 0:
    subset_data = df[df['Country/Region'].isin(country_name_input)]


# Filters UI
subset_data = df

country_name_input = st.sidebar.multiselect(
'Country name',
df.groupby('Country/Region').count().reset_index()['Country/Region'].tolist())
# by country name
if len(country_name_input) > 0:
    subset_data = df[df['Country/Region'].isin(country_name_input)]





# Widgets

st.write("This is a Slider")


x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

st.write("Checkbox with hidden content")

if st.checkbox('Show dataframe'):
    chart_data_2 = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data_2


st.write("Selectbox with options")

df2 = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df2['first column'])

