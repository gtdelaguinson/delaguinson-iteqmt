import streamlit as st
import pandas as pd
import pickle
from nltk.corpus import names

# Load the trained Naive Bayes classifier from the saved file
filename = 'pages/new_predict.sav'
loaded_model = pickle.load(open(filename, 'rb'))

# # Use the model to make predictions
@st.cache_data 
def predict_brand(features):
    st.text("The brand is " + brand_name)
    return
           
st.title("Laptop Brand Predictor")
st.subheader("Enter features to predict the laptop brand:")

# Slider inputs for features
price_input = st.slider("Price:", 0.0, 20000.0)
rating_input = st.slider("Rating:", 0.0, 20.0)
ram_input = st.slider("RAM (GB):", 0, 32)

# Button to trigger prediction
if st.button("Predict Brand"):
    features = [price_input, rating_input, ram_input]
    predict_brand(features)

st.text("The predicted brand will be displayed above.")
