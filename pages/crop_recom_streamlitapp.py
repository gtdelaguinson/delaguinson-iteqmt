#Notes
# do a "pip install streamlit" first 
#to run on terminal issue this command
# python -m streamlit run streamlit_test.py

import streamlit as st
import pandas as pd
import pickle
from nltk.corpus import names

# Load the trained Naive Bayes classifier from the saved file
filename = 'pages/predict.sav'
loaded_model = pickle.load(open(filename, 'wb'))

# # Use the model to make predictions
@st.cache_data 
def predict_crop():
    st.text("The brand is " + brand_name)
    return
           
st.title("Brand Predictor")
st.subheader("Input Features:")
price_input = st.slider("Price:", 0.0, 20000.0)
rating_input = st.slider("Rating:", 0.0, 20.0)
ram_input = st.slider("RAM (GB):", 0, 32)
if st.button("Predict Brand"):
    features = [price_input, rating_input, ram_input]
    predict_brand(features)
else:
    crop_name = loaded_model.predict([[pd.to_numeric(n_input),pd.to_numeric(p_input),pd.to_numeric(k_input)]])

st.text("The predicted brand will be displayed above.")
st.text_area(label ="",value=crop_name, height =100)
# st.button('Predict', on_click=predict_crop
