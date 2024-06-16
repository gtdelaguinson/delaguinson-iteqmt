import streamlit as st
import pickle

# Load the trained Naive Bayes classifier from the saved file
filename = 'pages/crop_recom_model.sav'

try:
    with open(filename, 'rb') as file:
        loaded_model = pickle.load(file)
except FileNotFoundError:
    st.error(f"Model file '{filename}' not found. Please make sure the file path is correct.")
    st.stop()
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Function to predict crop based on input NPK levels
def predict_crop(n_input, p_input, k_input):
    if n_input == 0 and p_input == 0 and k_input == 0:
        return "Please enter non-zero values for NPK levels."  # Informative message for empty input
    else:
        try:
            # Predict using the loaded model
            crop_name = loaded_model.predict([[n_input, p_input, k_input]])
            return crop_name[0]  # Return the predicted crop name
        except Exception as e:
            return f"Prediction error: {e}"

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
st.text("Predicted crop based on NPK levels:")
st.text(crop_name)
