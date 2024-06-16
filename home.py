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
     

### 💾 Machine Learning

##### 💻 Applications

* Prediction
* Sentiment Analysis
* Image Classification



### 🔎 Overview""", unsafe_allow_html=True)


st.image("./IMAGE2.png")


st.markdown("""
This application is designed to analyze the sentiment expressed in text messages. It utilizes a trained Naive Bayes classifier to classify text into positive, negative, or neutral sentiments based on the words used.

How it Works:

Input: Users input their name and describe how they are feeling today in the provided text boxes.
Analysis: The application examines the words in the input message to determine its sentiment.
Classification: Words are compared against predefined lists of positive, negative, and neutral words. If a match is found, the sentiment is displayed accordingly.
Feedback: Additionally, users receive motivational messages tailored to their sentiment to uplift their mood.
Output: The application outputs the user's name along with an assessment of their sentiment and an encouraging message.
Key Features:

Customizable: Users can input their name and express their feelings freely.
Real-time Analysis: Sentiment analysis is performed instantly upon clicking the "Analyze Sentiment" button.
Feedback: Users receive personalized messages to help them feel better based on their sentiment.
Try it Out:

Enter your name.
Describe how you are feeling today.
Click the "Analyze Sentiment" button to receive feedback.
Feel free to express yourself and see how the Sentiment Analyzer responds!
   
""", unsafe_allow_html=True)

st.image("./IMAGE.png")
st.markdown("""
This web application leverages a machine learning model to classify uploaded images based on food categories. Using a pre-trained model, it analyzes features extracted from images to predict and display the category of food depicted.

How it Works:

Input: Users upload an image containing food items using the sidebar file uploader.

Analysis: The application extracts visual features from the uploaded image using a deep learning model.

Classification: The extracted features are processed through a trained classifier, which predicts the category of food in the image.

Output: The predicted food category is displayed alongside the uploaded image, providing instant classification results.

Key Features:

Efficient Classification: Utilizes image embeddings for accurate food category prediction.
User-friendly Interface: Simple file upload interface with real-time classification feedback.
Scalable: Handles image uploads up to 5MB in size for comprehensive food image analysis.
Try it Out:

Upload: Select an image file containing food items.
Predict: Click the "Predict Category" button to see the predicted food category.
Explore: Explore various food images and see how accurately they are classified!
Explore the world of food through the lens of machine learning with our Image Classification for Food web application!
""", unsafe_allow_html=True)


hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
