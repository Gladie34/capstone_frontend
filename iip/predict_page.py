import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('xgb_model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)
    return loaded_model

#loaded_model=load_model #execute the model

def show_predict_page():
    st.title("Loan prediction approval ")
    st.write("""### we need some information to check on your loan approvals""")

    with st.sidebar:
        loan_id=st.number_input("Load Id",placeholder="Type a number...")
        no_of_dependents=st.number_input("No of dependents",placeholder="Type a number...")
        education=st.selectbox("Education Level",options=["Graduate","Not Graduate"],placeholder="Select Education level...")
        self_employed=st.selectbox("Self-Employed",options=["Yes","No"],placeholder="select...")
        income_annum=st.number_input("Annual Income",placeholder="Type a number....")
        loan_amount=st.number_input("Amount of Loan",placeholder="Enter Loan amount...")
        loan_term=st.number_input("Loan Term",placeholder="Enter loan terms in months...")
        cibil_score=st.number_input("Cibil Score",placeholder="Enter  your cibil score")
        residential_assets_value=st.number_input("Residential Asset Value",placeholder="Enter the value of your residential asset..")
        commercial_assets_value=st.number_input("Commercial Assets Value",placeholder="Enter your commercial asset value...")
        luxury_assets_value=st.number_input("Luxury Assets Value",placeholder="Enter your luxury asset value...")
        bank_assets_value=st.number_input("Bank Assets Value",placeholder="Enter your bank asset value...")