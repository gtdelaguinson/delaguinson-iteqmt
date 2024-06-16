import pickle
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

data = pd.read_csv('pages/laptops.csv')
X =data[['Price','Rating','ram_memory']]
Y = data ['brand']

model = RandomForestClassifier(n_estimators=100)
model.fit(X, Y)

filename = '/pages/predict.sav'
pickle.dump(model, open(filename,'wb'))

import pickle

filename = '/pages/predict.sav'  # Make sure this path is correct
loaded_model = pickle.load(open(filename, 'rb'))

features = [150,20000,25]
predicted_team = loaded_model.predict([features])
print(f'The predicted team is {predicted_team[0]}')

import streamlit as st
import pandas as pd
import pickle

# Load the trained model/content/drive/MyDrive/Dataset/laptops.csv
filename = '/pages/predict.sav'  # Make sure this path is correct
loaded_model = pickle.load(open(filename, 'rb'))

# Function to predict laptop brand
def predict_brand(features):
    brand_name = loaded_model.predict([features])[0]
    st.text(f"The predicted brand is {brand_name}")

# Streamlit app
st.title("Laptop Brand Predictor")
st.subheader("Enter features to predict the laptop brand:")

# Slider inputs for features
price_input = st.slider("Price:", 0.0, 20000.0)
rating_input = st.slider("Rating:", 0.0, 20.0)
ram_input = st.slider("RAM (GB):", 0, 32)  # Assuming RAM input in GB

# Button to trigger prediction
if st.button("Predict Brand"):
    features = [price_input, rating_input, ram_input]
    predict_brand(features)

st.text("The predicted brand will be displayed above.")
