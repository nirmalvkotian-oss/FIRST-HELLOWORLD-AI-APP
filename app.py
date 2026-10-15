import streamlit as st
import numpy as np
from model import train

#Title
st.title("Hello World AI App")
st.subheader("A simple regression model ")

#Train model
model = train()

#SIDEBAR
st.sidebar.header("Input features")
input_value=st.sidebar.slider(" Select value f x ", 1,10,1)
#prediction
input_array=np.array([[input_value]])
Prediction=model.predict(input_array)

#display result
st.write(f'### Input value : {input_value}')
st.write(f'### Output value: {Prediction[0][0]:.2f}')