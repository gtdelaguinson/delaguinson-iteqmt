import pickle
from PIL import Image
from img2vec_pytorch import Img2Vec
import streamlit as st

# Setting page configuration
st.set_page_config(layout="wide", page_title="Image Classification for Foods")

# Title and description
st.write("## Image Classification Model for Foods")
st.write(":grin: Predicting food categories from uploaded images :grin:")

# Sidebar for uploading images
st.sidebar.write("## Upload an Image")
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB maximum file size

# Load the pre-trained model
model_file = '/content/model_needs_npk.p'
try:
    with open(model_file, 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error(f"Model file '{model_file}' not found. Please make sure the file exists.")
    st.stop()
except Exception as e:
    st.error(f"Error loading the model: {str(e)}")
    st.stop()

# Initialize Img2Vec
img2vec = Img2Vec()

# Function to classify uploaded image
@st.cache(allow_output_mutation=True)
def classify_image(upload):
    image = Image.open(upload)
    st.write("### Image to be predicted:")
    st.image(image)

    st.write("### Predicted Category:")
    try:
        features = img2vec.get_vec(image)
        pred = model.predict([features])[0]
        st.header(pred)  # Display the predicted category
    except Exception as e:
        st.error(f"Error predicting image category: {str(e)}")

# Layout for the app
col1, col2 = st.columns(2)
my_upload = col1.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# Process uploaded image
if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
    else:
        classify_image(my_upload)
else:
    st.write("Upload an image to classify it.")
