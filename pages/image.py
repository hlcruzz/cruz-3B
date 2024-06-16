import streamlit as st
from PIL import Image
import pickle
from sklearn.model_selection import GridSearchCV

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

# Function to extract the underlying model
def extract_model(model):
    if isinstance(model, GridSearchCV):
        # Use the GridSearchCV object directly if best_estimator_ is not available
        return model
    else:
        # If not a GridSearchCV object, return as-is
        return model

# Load the model
model = load_model()

# Extract the underlying model
svc_model = extract_model(model)

# Streamlit Web App Interface
st.write("## Fruits Classification Model 🍎")
st.write("Upload an image of a fruit, and we'll predict its category based on our trained model!")
st.sidebar.write("## Upload and Download")

# Streamlit columns for displaying the image and prediction
col1, col2 = st.columns(2)

# File uploader in the sidebar
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# Handling the uploaded file
if my_upload is not None:
    # Display uploaded image
    image = Image.open(my_upload)
    col1.write("### Uploaded Image :camera:")
    col1.image(image, use_column_width=True)
    
    # Placeholder for predicted category
    col2.write("### Predicted Category :wrench:")
    col2.write("Please wait while the model is loading or there's an issue with the model.")
else:
    st.write("## Welcome!")
    st.write("Upload an image to get started.")
    st.write("This app is developed by Harold Cruz.")
