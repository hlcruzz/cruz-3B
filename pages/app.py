
import streamlit as st
import pandas as pd
import pickle
from nltk.corpus import names
from sklearn.metrics._scorer import _SCORERS

# Load the trained Naive Bayes classifier from the saved file
# Since we are using Google Colab, don't forget to upload your file
filename = 'crop_recom_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

st.title("Crop Recommendation Predictor :smile:")
st.subheader("Enter a set of NPK levels to determine what crop best fits:")
n_input = st.slider("Nitrogen: ",0,500)
p_input = st.slider("Phosphorus: ",0,500)
k_input = st.slider("Potassium: ",0,500)
if n_input == 0 & p_input == 0 & k_input == 0:
    crop_name = ""
else:
    crop_name = loaded_model.predict([[pd.to_numeric(n_input),pd.to_numeric(p_input),pd.to_numeric(k_input)]])
    # crop_name = "testing"

st.text("The crop suitable for this NPK level:")
st.text_area(label ="",value=crop_name, height =100)
# st.button('Predict', on_click=predict_crop
