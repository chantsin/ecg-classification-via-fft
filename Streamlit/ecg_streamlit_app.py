# ecg_streamlit_app

### IMPORT LIBRARIES
import pandas as pd 
import matplotlib.pyplot as plt
import streamlit as st 
import joblib

# Set app title 

main_title = 'ECG Classification'

st.set_page_config(
    page_title=main_title, 
    page_icon="🧊",
    layout='wide')

st.title('ECG Classification via Fourier Transforms 🫀') 