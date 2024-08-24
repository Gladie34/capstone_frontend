import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('xgb_model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)
    return loaded_model

#loaded_model=load_model #execute the model

def show_predict_page():
    st.title("Loan prediction approval")
    st.write("""### we need some information to check on your loan approvals""")
