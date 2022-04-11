import streamlit as st
import numpy as np
import pandas as pd

st.write("Here's our first attempt at using data to create a table:")

st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

st.write("DataFrame with highlight_max:")

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

st.write("Line chart")

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.write("Plot a map")

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

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

