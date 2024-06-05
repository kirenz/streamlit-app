# Importing the Streamlit package which is used to create web applications
import streamlit as st

# Importing custom modules for different pages of the application
import page_one
import page_two
import page_three
import page_four


# Defining a dictionary that maps page names to their respective modules
PAGES = {
    "User Persona": page_one,   # Key-value pair for the first page
    "Unternehmensdaten": page_two,   # Key-value pair for the second page
    "Kennzahlen": page_three, # Key-value pair for the third page
    "Datenübersicht": page_four, # Key-value pair for the fourth page

}

# Creating a sidebar in the web application for navigation
st.sidebar.title('Navigation')

# Adding a radio button widget to the sidebar for selecting a page
# The keys of the PAGES dictionary are used as the options
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# Getting the module of the selected page
page = PAGES[selection]

# Calling the 'app' function from the selected page's module to display the page content
page.app()