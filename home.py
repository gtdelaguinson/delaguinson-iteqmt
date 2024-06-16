import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

# Function to add custom CSS to hide Streamlit menu and footer
def hide_streamlit_style():
    st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Function to display page titles
def display_page_titles():
    st.markdown("""
    # Machine Learning Applications

    ## Overview
    """, unsafe_allow_html=True)

    st.markdown("""
    ### Applications

    #### Prediction
    The Prediction app allows users to predict outcomes based on input data. It's useful for making forecasts and estimates in various fields.

    #### Sentiment Analysis
    The Sentiment Analysis app analyzes text sentiment (positive, negative, or neutral) to provide insights into emotions expressed in written content.

    #### Image Classification
    The Image Classification app categorizes images based on their content using advanced algorithms and deep learning techniques.
    """, unsafe_allow_html=True)

    st.markdown("""
    ## About Me

    I am a curious and compassionate individual who loves to explore new ideas and connect with others. My passion for learning drives me to constantly seek out knowledge and understanding. I believe in the power of kindness and empathy to make a positive impact in the world.
    """, unsafe_allow_html=True)

# Define pages and sections
add_page_title()
show_pages([
    Page("home.py"),
    Section("Applications"),
    Page("pages/crop_recom_streamlitapp.py", "Prediction", "1️⃣", in_section=True),
    Page("pages/basic_sentiment_analyzer.py", "Sentiment Analysis", "2️⃣", in_section=True),
    Page("pages/img_classification.py", "Image Classification", "3️⃣", in_section=True),
    Section("SRC"),
    Page("pages/crop_src.py", "Prediction Source", "1️⃣", in_section=True),
    Page("pages/sentiment_src.py", "Sentiment Analysis Source", "2️⃣", in_section=True),
    Page("pages/image_classification_src.py", "Image Classification Source", "3️⃣", in_section=True),
])

# Render the page titles and descriptions
display_page_titles()

# Apply custom CSS to hide Streamlit menu and footer
hide_streamlit_style()
