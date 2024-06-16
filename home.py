import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

add_page_title()
show_pages(
    [   
        Page("home.py",),
        Section("Applications"),
        Page("pages/crop_recom_streamlitapp.py", "Prediction", "1️⃣", in_section=True),
        Page("pages/basic_sentiment_analyzer.py", "Sentiment Analysis", "2️⃣", in_section=True),
        Page("pages/img_classification.py", "Image Classification", "3️⃣", in_section=True),

        
        Section("SRC"),
        Page("pages/crop_src.py", "Prediction Source", "1️⃣", in_section=True),
        Page("pages/sentiment_src.py", "Sentiment Analysis Source", "2️⃣", in_section=True),
        Page("pages/image_classification_src.py", "Image Classification Source", "3️⃣", in_section=True),

    ]
)



st.markdown("""

About Me:

I am a curious and compassionate individual who loves to explore new ideas and connect with others. My passion for learning drives me to constantly seek out knowledge and understanding. I believe in the power of kindness and empathy to make a positive impact in the world.
     

### Machine Learning

##### Applications

* Prediction
* Sentiment Analysis
* Image Classification



### Overview""", unsafe_allow_html=True)






hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
