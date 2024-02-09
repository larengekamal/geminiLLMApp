from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os 
import google.generativeai as genai 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load gemini pro model and get response
model = genai.GenerativeModel('gemini-pro')
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

## Initialize streamlit app
st.set_page_config(page_title="Gemini Pro Model App")
st.header('Gemini LLM Application')
input=st.text_input('Input: ', key='input')
submit=st.button('Ask the Question')

## When submit is clicked
if submit:
    response=get_gemini_response(input)
    st.subheader('Response is:')
    st.write(response)


