# -------------------#
# SETUP
import streamlit as st
import pandas as pd
import altair as alt
from vega_datasets import data

# -------------------#
# IMPORT DATA

df = pd.read_csv(
    "https://raw.githubusercontent.com/kirenz/datasets/master/oecd-new.csv")

### -------------------###
# START OF OUR APP

# -------------------#
# HEADER
# Title of our app
st.title("Hello World")
# Add header
st.header("My Text")
# -------------------#
# SIDEBAR
# Header
st.sidebar.header("This is my sidebar")
# MULTISELECT
COUNTRY = df['country'].to_list()
#selected_country = COUNTRY
selected_country = st.sidebar.multiselect(
    'Select', COUNTRY)
# Filter the DataFrame based on the selected countries
filtered_df = df[df['country'].isin(selected_country)]

# -------------------#
# BODY

# Check if the user has made a selection
if selected_country:
    # If the user has selected countries, filter the DataFrame
    filtered_df = df[df['country'].isin(selected_country)]
else:
    # If no selection is made, use the complete DataFrame
    filtered_df = df
    
st.write("Take a look at my data")
# Show filtered DataFrame
st.dataframe(filtered_df)

st.write("Take a look at my chart")
# Make a chart with altair

c = alt.Chart(filtered_df).mark_circle().encode(
    x='life_satisfaction',
    y='gdp_per_capita',
    color='country'
)

# Show plot
st.altair_chart(c, use_container_width=True)

### -------------------###
st.title("Interactive Rectangular Brush Plot")


st.markdown("You can use *Markdown* to **explain** the ***content***.")
st.markdown('''
    :red[Example] :orange[shows] :green[how] :blue[to] :violet[add]
    :gray[a simple] :rainbow[rectangular brush to a scatter plot].''')


multi = '''By clicking and dragging on the plot,  
you can highlight points within the range.

'''
st.markdown(multi)


# Make a chart with altair
brush = alt.selection_interval()

c2 = alt.Chart(df).mark_point().encode(
    x='life_satisfaction',
    y='gdp_per_capita',
    color=alt.condition(brush, 'country', alt.value('grey')),
).add_params(brush)

# Show plot
st.altair_chart(c2, use_container_width=True)


st.title("Streamlit emoji")

st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")


st.markdown("[Streamlit emoji shortcodes](https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app)")


### -------------------###

st.title('Multiple Interactions')


movies = alt.UrlData(
    data.movies.url,
    format=alt.DataFormat(parse={"Release_Date":"date"})
)
ratings = ['G', 'NC-17', 'PG', 'PG-13', 'R']
genres = [
    'Action', 'Adventure', 'Black Comedy', 'Comedy',
    'Concert/Performance', 'Documentary', 'Drama', 'Horror', 'Musical',
    'Romantic Comedy', 'Thriller/Suspense', 'Western'
]

base = alt.Chart(movies, width=200, height=200).mark_point(filled=True).transform_calculate(
    Rounded_IMDB_Rating = "floor(datum.IMDB_Rating)",
    Hundred_Million_Production =  "datum.Production_Budget > 100000000.0 ? 100 : 10",
    Release_Year = "year(datum.Release_Date)"
).transform_filter(
    alt.datum.IMDB_Rating > 0
).transform_filter(
    alt.FieldOneOfPredicate(field='MPAA_Rating', oneOf=ratings)
).encode(
    x=alt.X('Worldwide_Gross:Q').scale(domain=(100000,10**9), clamp=True),
    y='IMDB_Rating:Q',
    tooltip="Title:N"
)

# A slider filter
year_slider = alt.binding_range(min=1969, max=2018, step=1, name="Release Year")
slider_selection = alt.selection_point(bind=year_slider, fields=['Release_Year'])

filter_year = base.add_params(
    slider_selection
).transform_filter(
    slider_selection
).properties(title="Slider Filtering")

# A dropdown filter
genre_dropdown = alt.binding_select(options=genres, name="Genre")
genre_select = alt.selection_point(fields=['Major_Genre'], bind=genre_dropdown)

filter_genres = base.add_params(
    genre_select
).transform_filter(
    genre_select
).properties(title="Dropdown Filtering")

#color changing marks
rating_radio = alt.binding_radio(options=ratings, name="Rating")
rating_select = alt.selection_point(fields=['MPAA_Rating'], bind=rating_radio)

rating_color_condition = alt.condition(
    rating_select,
    alt.Color('MPAA_Rating:N').legend(None),
    alt.value('lightgray')
)

highlight_ratings = base.add_params(
    rating_select
).encode(
    color=rating_color_condition
).properties(title="Radio Button Highlighting")

# Boolean selection for format changes
input_checkbox = alt.binding_checkbox(name="Big Budget Films ")
checkbox_selection = alt.param(bind=input_checkbox)

size_checkbox_condition = alt.condition(
    checkbox_selection,
    alt.Size('Hundred_Million_Production:Q'),
    alt.SizeValue(25)
)

budget_sizing = base.add_params(
    checkbox_selection
).encode(
    size=size_checkbox_condition
).properties(title="Checkbox Formatting")

(filter_year | filter_genres) & (highlight_ratings | budget_sizing)




# END OF APP
