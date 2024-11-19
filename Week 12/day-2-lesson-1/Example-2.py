
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import base64
import os
import streamlit as st

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=GEMINI_API_KEY)

def encode_image(image_file):
        return base64.b64encode(image_file.read()).decode()

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that can describe images."),
        (
            "human",
            [
                {"type": "text", "text": "{input}"},
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

st.title("Image Analysis Using Gemini")

col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("Upload your image", type=["jpg", "png"])

with col2:
    if uploaded_file is not None:
         st.image(uploaded_file)
    else:
         st.write("No image uploaded")

question = st.text_input("Enter a question")

if question and uploaded_file != None:
     image = encode_image(uploaded_file)
     res = chain.invoke({"input": question, "image": image})
     st.write(res.content)