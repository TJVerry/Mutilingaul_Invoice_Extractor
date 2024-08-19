import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from PIL import Image


# Load the environment variables
load_dotenv()
# print(os.getenv("GOOGLE_API_KEY"))

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load the model
model = genai.GenerativeModel("gemini-1.5-pro")

def generate_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text

def image_setup(image):
    if image is not None:
        # Read file into bytes
        bytes_data = image.getvalue()

        image_parts = [
            {
                "mime_type": image.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        return FileNotFoundError ("No image uploaded")

# Streamlit app
st.set_page_config(page_title="Multilanguage Invoice Extractor", page_icon="💸")
st.header("Multilanguage Invoice Extractor")
input = st.text_input("What can I help you with today?", key = 'input')
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"], key = 'image')
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

submit = st.button("Ask Gemini")

input_prompt = """
You are an expert in understanding invoices. You have been asked to extract the following information from the invoice: 
"""

if submit:
    image_data = image_setup(uploaded_file)
    response = generate_response(input_prompt, image_data, input)
    st.write(response)

