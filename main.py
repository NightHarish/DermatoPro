"""This is the main module to run the app"""

# Importing the necessary Python modules.
import streamlit as st

# Import necessary functions from web_functions
from web_functions import load_data

# Configure the app
st.set_page_config(
    page_title = 'Dermatological Risk Prediction',
    page_icon = 'random',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)

# Import pages
from Tabs import home, data, predict, visualise



# Dictionary for pages
Tabs = {
    "Home": home,
    "Data Info": data,
    "Prediction": predict,
    "Visualisation": visualise
    
}

# Create a sidebar
# Add title to sidear
st.sidebar.title("Navigation")

# Create radio option to select the page
page = st.sidebar.radio("Pages", list(Tabs.keys()))

# Loading the dataset.
df, X, y = load_data()

# Call the app funciton of selected page to run
if page in ["Prediction", "Visualisation"]:
    Tabs[page].app(df, X, y)
elif (page == "Data Info"):
    Tabs[page].app(df)
else:
    Tabs[page].app()


# Skin Disease Detection
st.sidebar.markdown(
    f'<a href="https://dermatrix.streamlit.app/" target="_blank" style="display: inline-block; padding: 12px 20px; background-color: #4CAF50; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px;">Skin Disease Detection</a>',
    unsafe_allow_html=True
)

# Skin Type Detection
st.sidebar.markdown(
    f'<a href="https://skin-type-detector.streamlit.app/" target="_blank" style="display: inline-block; padding: 12px 20px; background-color: blue; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px;">Skin Type Detection</a>',
    unsafe_allow_html=True
)