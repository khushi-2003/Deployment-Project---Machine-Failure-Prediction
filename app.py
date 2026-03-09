import streamlit as st
import joblib
import pandas as pd

#set the tab title
st.set_page_config("ML project")

#set the page title
st.title("Machine Failure Predictions")

#sub-header
st.subheader("By Khushi Kanade")

#Load preprocessor pipeline and model
preprocessor = joblib.load('pre.joblib')
model =joblib.load('model_grad.joblib')

#creating input boxes for user input 
Type = st.selectbox('Type',options=['L','M','H'])
AirTemp = st.number_input('AirTemp',min_value=0)

ProcessTemp = st.number_input('ProcessTemp',min_value=0)

RPM= st.number_input('RPM',min_value=0,step=1)

torque= st.number_input('torque',min_value=0)

ToolWear= st.number_input('ToolWear',min_value=0,step=1)

TWF = st.number_input('TWF',min_value=18,step=1)

HDF= st.number_input('HDF',min_value=18,step=1)

PWF=st.number_input('PWF',min_value=18,step=1)

OSF = st.number_input('OSF',min_value=18,step=1)

RNF = st.number_input('RNF',min_value=18,step=1)


#submit button
submit = st.button('Predict Machine Failure ')

if submit:
    data = {
        'Type' :[Type],
        'Air temperature [K]': [AirTemp], 
        'Process temperature [K]' : [ProcessTemp],
        'Rotational speed [rpm]' : [RPM],
        'Torque [Nm]' : [torque], 
        'Tool wear [min]': [ToolWear],
        'TWF' : [TWF],
        'HDF' : [HDF],
        'PWF' : [PWF],
        'OSF' : [OSF], 
        'RNF' : [RNF]
    }

    df_data = pd.DataFrame(data)
    #apply data cleaning and preprocessing on new user data
    data_pre=  preprocessor.transform(df_data)

    pred = model.predict(data_pre)
    if pred[0]==1:
        op = 'Machine would fail'
    else:
        op='Machine would not fail'
    st.subheader(op)