import streamlit as st
import pandas as pd
import pickle
from nltk.corpus import names

# Load the trained Naive Bayes classifier from the saved file
filename = 'pages/crop_recom_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

# Function to predict crop based on input NPK levels
def predict_crop(n_input, p_input, k_input):
    if n_input == 0 and p_input == 0 and k_input == 0:
        return ""  # Return empty string if all inputs are zero
    else:
        # Predict using the loaded model
        crop_name = loaded_model.predict([[n_input, p_input, k_input]])
        return crop_name[0]  # Return the predicted crop name

# Streamlit app
st.title("Crop Recommendation Predictor 😊")
st.subheader("Enter a set of NPK levels to determine the best crop:")

# Input sliders for NPK levels
n_input = st.slider("Nitrogen", 0, 500)
p_input = st.slider("Phosphorus", 0, 500)
k_input = st.slider("Potassium", 0, 500)

# Predicting the crop
crop_name = predict_crop(n_input, p_input, k_input)

# Display the predicted crop name
st.text("The crop suitable for this NPK level:")
st.text_area(label="", value=crop_name, height=1)

# Note: No need for st.cache_data decorator here as we are not caching the function predict_crop itself
