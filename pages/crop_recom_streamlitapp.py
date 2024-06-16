import streamlit as st
import pandas as pd
import pickle

# Load the trained model
filename = 'pages/predict.sav'
loaded_model = pickle.load(open(filename, 'rb'))  # Correct mode is 'rb'

# Function to predict laptop brand
def predict_brand(features):
    brand_name = loaded_model.predict([features])[0]
    st.text(f"The predicted brand is {brand_name}")

# Streamlit app
st.title("Brand Predictor")
st.subheader("Input Features:")

# Slider inputs for features
price_input = st.slider("Price:", 0.0, 20000.0)
rating_input = st.slider("Rating:", 0.0, 20.0)
ram_input = st.slider("RAM (GB):", 0, 32)

# Button to trigger prediction
if st.button("Predict Brand"):
    features = [price_input, rating_input, ram_input]
    predict_brand(features)

st.text("The predicted brand will be displayed above.")
