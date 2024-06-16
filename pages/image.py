import torch
from torchvision import transforms
from img2vec_pytorch import Img2Vec
import streamlit as st
from PIL import Image
from io import BytesIO
import pickle
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

# Set Streamlit page configuration
st.set_page_config(layout="wide", page_title="Image Classification for Fruits")

# Function to load the GridSearchCV model
def load_model():
    try:
        with open('pages/model.p', 'rb') as f:
            model = pickle.load(f)
        return model
    except FileNotFoundError:
        st.error("Model file not found. Please upload the model file.")
        return None
    except Exception as e:
        st.error(f"Error loading the model: {e}")
        return None

# Function to extract the best estimator from GridSearchCV
def extract_best_estimator(model):
    if isinstance(model, GridSearchCV):
        best_estimator = model.best_estimator_
        if isinstance(best_estimator, SVC):
            return best_estimator
        else:
            st.error("Best estimator is not an instance of SVC. Check the content of model.p.")
            return None
    else:
        st.error("Loaded model is not a GridSearchCV object. Check the content of model.p.")
        return None

# Load the GridSearchCV model
model = load_model()

# Extract the best estimator (assuming it's an SVC model)
svc_model = extract_best_estimator(model)

# Initialize Img2Vec with the SVC model
try:
    img2vec = Img2Vec(model=svc_model)
except Exception as e:
    st.error(f"Error initializing Img2Vec with the loaded SVC model: {e}")
    st.stop()

# Streamlit Web App Interface
st.write("## Fruits Classification Model")
st.write("Upload an image of a fruit, and we'll predict its category based on our trained model!")
st.sidebar.write("## Upload and Download")

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

# Function to convert the image to bytes
@st.cache
def convert_image_to_bytes(img):
    buf = BytesIO()
    img.save(buf, format="JPEG")
    byte_im = buf.getvalue()
    return byte_im

# Function to process and predict the uploaded image
def predict_image(upload):
    image = Image.open(upload)
    st.sidebar.write("### Image to be Predicted :camera:")
    st.sidebar.image(image, use_column_width=True)

    st.sidebar.write("### Predicted Category :wrench:")
    try:
        features = img2vec.get_vec(image)
        # Assuming img2vec.get_vec() returns features as needed
        # Perform prediction with svc_model
        pred = svc_model.predict([features])
        st.sidebar.header(pred[0])
    except Exception as e:
        st.error(f"Error during prediction: {e}")

# Streamlit columns for displaying the image and prediction
col1, col2 = st.columns(2)

# File uploader in the sidebar
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# Handling the uploaded file
if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
    else:
        if svc_model is not None:
            predict_image(upload=my_upload)
else:
    st.write("## Welcome!")
    st.write("Upload an image to get started.")
    st.write("This app is developed by Harold Cruz.")
