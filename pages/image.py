import pickle
import torch
from torchvision import models
from img2vec_pytorch import Img2Vec
import streamlit as st

# Set Streamlit page configuration
st.set_page_config(layout="wide", page_title="Image Classification for Fruits")

# Function to load the model
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

# Function to check if the model is fitted
def is_model_fitted(model):
    try:
        check_is_fitted(model)
        return True
    except NotFittedError:
        return False

# Load the model
model = load_model()

# Initialize Img2Vec with pretrained ResNet18
try:
    # Load pretrained ResNet18 from TorchVision
    resnet18 = models.resnet18(pretrained=True)
    
    # Initialize Img2Vec with ResNet18
    img2vec = Img2Vec(model=resnet18)
    
except Exception as e:
    st.error(f"Error initializing Img2Vec with ResNet18: {e}")
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
    features = img2vec.get_vec(image)
    try:
        if model is not None and is_model_fitted(model):
            pred = model.predict([features])
            st.sidebar.header(pred[0])
        else:
            st.error("The model is not fitted. Please fit the model before using it for predictions.")
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
        if model is not None:
            predict_image(upload=my_upload)
else:
    st.write("## Welcome!")
    st.write("Upload an image to get started.")
    st.write("This app is developed by Harold Cruz.")

