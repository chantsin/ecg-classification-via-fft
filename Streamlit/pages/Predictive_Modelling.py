import streamlit as st
import pandas as pd
import numpy as np
import joblib
import pickle

st.sidebar.markdown("# ECG Prediction")
st.sidebar.markdown(
"Given an ECG signal, we can use our model to predict the diagnostic of the \
with high accuracy."
)
        
st.title("ECG Prediction")

########################### PREDICTIVE MODELLING ###############################

metadata = pd.read_csv('../data/cleaned_metadata.csv')

# Load pickle model
# model = pickle.load(open('../Models/rnn_binary.pkl', 'rb'))

# Load the model using joblib
model = joblib.load('../Models/rnn_binary.pkl')

##### USER INPUT SELECTION #####

# Age
age = st.selectbox(
    'Age',
    tuple(str(num) for num in range(2, 90))
)
st.write(f'You selected: {age}.')

# Sex
sex = st.selectbox(
    'Sex',
    ('Male', 'Female')
)
st.write(f'You selected: {sex}.')

# Height
height = st.selectbox(
    'Height (cm)',
    tuple(str(height) for height in np.sort(metadata['height'].unique()))
)
st.write(f'You selected: {height} cm.')

# Weight
weight = st.selectbox(
    'Weight (kg)',
    tuple(str(weight) for weight in np.sort(metadata['weight'].unique()))
)
st.write(f'You selected: {weight} kg.')





