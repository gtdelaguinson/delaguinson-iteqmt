import streamlit as st
import pandas as pd
import pickle
from nltk.corpus import names

st.header('Simple Sentiment Analyzer App')
st.subheader('This python code is implemented for Streamlit')
st.code('''
import streamlit as st

# Set page title and subtitle
st.title("Sentiment Analyzer")
st.subheader("Enter your name and how you feel today")

# Input fields for name and message
name = st.text_input("What's your name?")
message = st.text_area("Tell me what you feel today")

# Lists of positive and negative words
positive_words = ['good', 'excited', 'happy', 'great', 'fantastic', 'wonderful']
negative_words = ['bad', 'sad', 'angry', 'terrible', 'awful', 'miserable']

# Function to analyze sentiment and display result
def analyze_sentiment(name, message):
    if not name or not message:
        st.warning("Please enter both your name and how you feel today.")
        return

    st.markdown("---")  # Horizontal line for separation
    st.write(f"Hi, {name}!")

    # Convert message to lowercase and split into words
    words = message.lower().split()

    # Check for positive and negative words
    if any(word in positive_words for word in words):
        st.write("That's good! :smile:")
    elif any(word in negative_words for word in words):
        st.write("I hope you feel better soon. :disappointed:")
    else:
        st.write("Keep going! :neutral_face:")

# Button to trigger sentiment analysis
if st.button('Analyze Sentiment'):
    analyze_sentiment(name, message)

# Additional content or features can be added below

''')
