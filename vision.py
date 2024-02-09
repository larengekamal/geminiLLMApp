from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os 
import google.generativeai as genai 
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load gemini pro model and get response
model = genai.GenerativeModel('gemini-pro-vision')
def get_gemini_response(question, image):
    if question != "":
        response = model.generate_content([question, image])
    else:
        response = model.generate_content(image)    
    return response.text

## Initialize streamlit app
st.set_page_config(page_title="Gemini Pro Multi Model App")
st.header('Gemini LLM Image Model Application')
input=st.text_input('Input: ', key='input')
upload_file = st.file_uploader("Choose a file: ", type=['jpeg', 'jpg', 'png'])
image=""
if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image, caption='Upload Image.',use_column_width=True)
    
submit=st.button('Tell me about Image')

## When submit is clicked
if submit:
    response=get_gemini_response(input, image)
    st.subheader('Response is:')
    st.write(response)