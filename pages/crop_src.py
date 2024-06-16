import streamlit as st


st.header('Crop Recommendation App')
st.subheader('This model was trained using a dataset')
st.code('''
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
    try:
        # Validate inputs
        if not isinstance(n_input, (int, float)) or not isinstance(p_input, (int, float)) or not isinstance(k_input, (int, float)):
            return "Please enter numeric values for NPK levels."
        
        if n_input < 0 or p_input < 0 or k_input < 0 or n_input > 500 or p_input > 500 or k_input > 500:
            return "Please enter values within the range of 0 to 500 for NPK levels."

        # Predict using the loaded model
        crop_name = loaded_model.predict([[n_input, p_input, k_input]])
        return crop_name[0]  # Return the predicted crop name
    except Exception as e:
        return f"Prediction error: {e}"

# Streamlit app
st.title("Crop Predictor")
st.sidebar.subheader("Enter NPK levels:")

# Input sliders for NPK levels in the sidebar
n_input = st.sidebar.slider("Nitrogen", 0, 500, 0)
p_input = st.sidebar.slider("Phosphorus", 0, 500, 0)
k_input = st.sidebar.slider("Potassium", 0, 500, 0)

# Predicting the crop based on NPK levels
crop_name = predict_crop(n_input, p_input, k_input)

# Display the predicted crop name in the main area
st.subheader("Predicted crop:")
st.write(crop_name)
    ''')
