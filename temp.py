# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle
import streamlit as st

#loading the save model
loaded_model = pickle.load(open('D:/ml_trained_dataset/diabetes_model.sav', 'rb'))

#creating a function for prediction
def diabetes_prediction(input_data):
    
    #changing the inputdata to numpy array
    changed_input_data_as_numpy_array = np.asarray(input_data)
    
    #reshaping the input array
    reshaped_input_array = changed_input_data_as_numpy_array.reshape(1, -1)
    
    prediction = loaded_model.predict(reshaped_input_array)
    
    if(prediction[0]==0):
         return "the person is diabetic"
    else:
        return "the person is not diabetic"
    
    
def main():
    #giving a title
    st.title("check person is diabetic or not")
    
    #getting the input data from user
    pregnancies = st.text_input('Number of pregnancies')
    Glucose = st.text_input('Glucose level')
    BloodPressure = st.text_input('reading og ')
    SkinTickness = st.text_input('reading of skinthickness')
    Insulin = st.text_input('Number of pregnancies')
    BMI = st.text_input('Number of pregnancies')
    DiabetesPedigreeFunction = st.text_input('Number of pregnancies')
    AGE = st.text_input('Number of pregnancies')
    
    
    #code of execution
    diagnosis=''
    
    
    #creating a button for prediction
    if st.button("Diabetes test Result"):
        diagnosis = diabetes_prediction([pregnancies, Glucose, BloodPressure, SkinTickness, Insulin, BMI, DiabetesPedigreeFunction, BMI, AGE])
        
    st.success(diagnosis)
    
    
    if __name__ == '__main__':
        main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    