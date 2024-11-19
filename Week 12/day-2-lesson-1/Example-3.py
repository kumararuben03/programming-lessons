from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import base64
import os
import streamlit as st

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=GEMINI_API_KEY)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that can verify identification documents"),
        (
            "human",
            [
               {"type": "text", "text": "Verify the identification details"},
               {"type": "text", "text": "Name: {user_name}"},
               {"type": "text", "text": "DOB: {user_dob}"},
               {
                   "type": "image_url",
                   "image_url": {
                       "url": f"data:image/jpeg;base64,""{image}",
                       "detail": "low",
                   }
               }
            ]
        )
    ]
)

chain = prompt | llm

def encode_image(image_file):
        return base64.b64encode(image_file.read()).decode()

st.title("KYC Verification Application")

col1, col2 = st.columns(2)

with col1:
        uploaded_file = st.file_uploader("Upload your ID document", type=["jpg", "png"])

with col2:
        if uploaded_file != None:
                st.image(uploaded_file)
        else:
                st.write("Image Preview")

user_name = st.text_input("Enter your name")
user_dob = st.text_input("Enter your date of birth")

if uploaded_file != None and user_name and user_dob:
        image = encode_image(uploaded_file)
        res = chain.invoke({"user_name": user_name, "user_dob": user_dob, "image": image})
        st.write(res.content)