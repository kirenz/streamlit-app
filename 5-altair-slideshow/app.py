import streamlit as st
import streamlit.components.v1 as components
import altair as alt
from vega_datasets import data

cars = data.cars()

st.title('Altair Slideshow')

chart1 = alt.Chart(cars).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color='Origin:N'
)

chart2 = alt.Chart(cars).mark_bar().encode(
    x=alt.X('Miles_per_Gallon', bin=alt.Bin(maxbins=30)),
    y='count()',
    color='Origin'
)

chart3 = alt.Chart(cars).mark_area(opacity=0.3).encode(
    x=alt.X('Year', timeUnit='year'),
    y=alt.Y('ci0(Miles_per_Gallon)', axis=alt.Axis(title='Miles per Gallon')),
    y2='ci1(Miles_per_Gallon)',
    color='Origin'
).properties(
    width=800
)

html = open('slide.html', 'r').read()
css = open('style.css', 'r').read()
js = open('script.js', 'r').read()
html = html.format(
    css_styler=css,
    slide_script=js,
    vega_version=alt.VEGA_VERSION,
    vegalite_version=alt.VEGALITE_VERSION,
    vegaembed_version=alt.VEGAEMBED_VERSION,
    spec1=chart1.to_json(indent=None),
    spec2=chart2.to_json(indent=None),
    spec3=chart3.to_json(indent=None)

)

components.html(html, height=800,scrolling=True)