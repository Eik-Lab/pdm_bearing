import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import os
from transform_data import frequency, amplitude

st.title('Bearing analysis')

# --- Sidebar ---
# datasets = os.listdir('./data_csv')
datasets = ["H-A-1.csv", "H-B-1.csv", "I-A-1.csv", "I-B-1.csv", "O-A-1.csv", "O-B-1.csv"]
with st.sidebar:
    st.write("""
    Health of bearing:
    - H = Healthy
    - O = Outer defect
    - I = Inner defect
    """)
    st.write("""
    Speed pattern of bearing:
    - A = Increasing
    - B = Decreasing
    - C = Increasing then decreasing
    - D = Decreasing then increasing
    """)

    options = st.multiselect('Choose datasets to analyse', datasets, datasets[0])



# --- Fetch data ---
vibration_data = pd.DataFrame()
speed_data = pd.DataFrame()
url = "https://raw.githubusercontent.com/Eik-Lab/pdm_bearing/main/bearing_app/data_csv/"
for data_name in options:
    data = pd.read_csv(f'{url}{data_name}')
    vibration_data[data_name] = data['Vibration']
    speed_data[data_name] = data['Speed']



# --- Slider ---
n_datapoints = st.slider('Datapoints to show', 10000, 2*10**6, step=10000)
step = int(n_datapoints/10**4)



# --- Vibration plot ---
st.subheader('Vibration')
vib_trans = st.selectbox('Tranform data', ('Raw', 'Frequency', 'Frequency / Speed'), key='vib_trans')

vib_plot_data = vibration_data
if vib_trans == 'Frequency':
    vib_plot_data = frequency(vib_plot_data, 1000)

elif vib_trans == 'Frequency / Speed':
    vib_plot_data = frequency(vib_plot_data, 1000) / \
        frequency(speed_data, 1000)

st.line_chart(vib_plot_data.iloc[:n_datapoints:step])



# --- Speed plot ---
st.subheader('Speed')
spe_trans = st.selectbox('Transform data', ('Raw', 'Frequency'), key='spe_trans')

spe_plot_data = speed_data
if spe_trans == 'Frequency':
    spe_plot_data = frequency(spe_plot_data, 1000)

st.line_chart(spe_plot_data.iloc[:n_datapoints:step])



# --- Scatter plot ---
st.subheader('Frequency vs amplitude')

scatter_data = pd.DataFrame()
scatter_data['x'] = [amplitude(data, 1000) for label, data in vibration_data.iteritems()]
scatter_data['y'] = frequency(vibration_data, 1000).mean().values
scatter_data['color'] = [option[0] for option in options]
scatter_data['size'] = [10] * len(scatter_data)

alt_data = alt.Chart(scatter_data).mark_circle().encode(x='x', y='y', size='size', color='color')

st.altair_chart(alt_data, True)
