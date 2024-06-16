import streamlit as st
import pandas as pd
import pickle

# Load the trained Naive Bayes classifier from the saved file
filename = 'pages/crop_recom_model.sav'

try:
    loaded_model = pickle.load(open(filename, 'rb'))
except FileNotFoundError:
    st.error(f"Model file '{filename}' not found. Please check the file path.")
except Exception as e:
    st.error(f"Error loading model: {str(e)}")

st.title("Crop Recommendation Predictor 🌾")
st.subheader("Enter a set of NPK levels to determine what crop best fits:")

n_input = st.slider("Nitrogen: ", 0, 500)
p_input = st.slider("Phosphorus: ", 0, 500)
k_input = st.slider("Potassium: ", 0, 500)

if n_input == 0 and p_input == 0 and k_input == 0:
    crop_name = ""
else:
    # Predict crop based on user inputs
    try:
        crop_name = loaded_model.predict([[pd.to_numeric(n_input), pd.to_numeric(p_input), pd.to_numeric(k_input)]])
    except Exception as e:
        crop_name = f"Error predicting crop: {str(e)}"

st.text("The crop suitable for this NPK level:")
st.text(crop_name)
