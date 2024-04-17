# ecg_streamlit_app

### IMPORT LIBRARIES
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import streamlit as st 
import joblib
import wfdb
import altair as alt

import sys
sys.path.append('..')
from Notebooks import ecg_cleaning as c

# Set app title 

main_title = 'ECG Classification'

st.set_page_config(
    page_title=main_title, 
    page_icon="🧊",
    layout='centered')


st.sidebar.markdown("# About My Capstone")

st.title('ECG Classification via Fourier Transforms 🫀')

st.markdown("""
            
In this project I will walk you through how I used data science \
tools to solve a problem in the medical field. Let's dive right \
into it!

### Introduction

Biomedical signals have always played an important role in the medical field. \
One type of biomedical signal that you may be familiar with is an ECG or \
electrocardiogram. An ECG looks at how our heart functions by recording our \
heart rate and heart rhythm. Using these records, physicians can come to \
conclusions about whether a person is healthy or not, and if its the latter \
they can come up with a proper treatment outcome for the patient. 
            
### Problem Space

Traditionally, ECG signals are interpreted solely based on human \
readibility, and using these results doctors can pinpoint the next steps \
needed. However, this poses a risk in that although doctors are very \
professional in their line of work, they can make mistakes too. This can lead \
to misdiagnosis resulting in patients not receiving proper treatment. To \
counteract this issue, I proposed to use data science tools, specifically \
machine learning (ML) algorithms to predict ECG diagnostics. 
""")


# Create a sample ECG signal 
path = '../data/physionet.org/files/ptb-xl/1.0.3/records100/00000/'
ecg = '00004_lr'
file = path + ecg
metadata = pd.read_csv('../data/cleaned_metadata.csv', index_col=0)

signals, fields = wfdb.rdsamp(file, channels=[1])

sampling_frequency = fields['fs']  # Sampling frequency
sig_len = fields['sig_len'] # Signal length 
sig_name = fields['sig_name'] # Lead

time = np.arange(0, sig_len) / sampling_frequency

# First we get the sampling interval 
dt = 1/sampling_frequency

# Flatten the signal from 2D to 1D 
signals = signals.flatten()

# FFT returns a result not centered at zero, therefore we need to fftshift it to zero
signal_fft = np.fft.fftshift(np.fft.fft(signals) * dt)
freq = np.fft.fftshift(np.fft.fftfreq(sig_len, dt))

# Baseline removal
signal_bl = c.baseline_removal(signals, freq_start=0.1, freq_stop=1.5)

# Plotting sample ECG signal and the denoised version 
samp_ecg = pd.DataFrame(
    {
        'Time': time,
        'Original ECG': signals, 
        'Denoised ECG': signal_bl
    }
)

# col1, col2, col3, col4, col5 = st.columns(5)
# with col2:
#     st.line_chart(samp_ecg, x='Time', 
#                 y=['Original ECG', 'Denoised ECG'], 
#                 color=["#FF0000", "#0000FF"],
#                 width=900,
#                 height=500,
#                 use_container_width=False) 

st.markdown("#### Example ECG Signal")

### SAMPLE ECG PLOT
# st.line_chart(
#     samp_ecg, 
#     x='Time', 
#     y=['Original ECG', 'Denoised ECG'], 
#     color=["#FF0000", "#0000FF"],
#     width=700,
#     height=400,
#     use_container_width=True
# ) 

chart1 = alt.Chart(samp_ecg).mark_line(color='red').encode(
    x=alt.X('Time'),
    y=alt.Y('Original ECG'),
).interactive()

chart2 = alt.Chart(samp_ecg).mark_line(color='blue').encode(
    x=alt.X('Time'),
    y=alt.Y('Denoised ECG')
).interactive()

chart = alt.layer(chart1, chart2)

st.altair_chart(chart, theme="streamlit", use_container_width=True)

       

