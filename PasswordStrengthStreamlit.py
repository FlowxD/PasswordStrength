# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 17:52:39 2020

@author: Mandar Joshi
"""
import numpy as np
import streamlit as st 
import pickle


st.header("Check Your Password Strength")
user_input = st.text_input("Enter your password")
loaded_lr = pickle.load(open("lr.pkl", "rb"))
#user_input ="xy"
li= [user_input]

def word_divide_char(inputs):
    characters=[]
    for i in inputs:
        characters.append(i)
    return characters

loaded_vec = pickle.load(open("vectorizer.pkl", "rb"))



X_predict=np.array(li)
X_predict=loaded_vec.transform(X_predict)
y_pred=loaded_lr.predict(X_predict)


if y_pred==0:
    st.write("Poor 🤢")
elif y_pred==1:
    st.write("Average 😐")
else:
    st.write("Strong 😎")
    

