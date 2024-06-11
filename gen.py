import pickle
import streamlit as st
model1=pickle.load(open("index.pkl","rb"))
def myf1():
    st.title("Gender prediction")
    st.write("0 for female, 1 for male")
    Weight=st.number_input("Enter Weight(in kg):")
    Height=st.number_input("Enter Height(in cm):")
    pred=st.button("Predict Gender")
    if pred:
        op=model1.predict([[Height,Weight]])
        st.write("Index is: ",op[0])
myf1()