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
        ("system", "You are a nutrition expert specializing in providing personalized diet suggestions based on user details and preferences."),
        (
            "human",
            [
                {"type": "text", "text": "Please provide personalized diet suggestions."},
                {"type": "text", "text": "Additional details: {additional_details}"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,""{image}"},
                        "detail": "low",
                    
                }
            ]
        )
    ]
)


chain = prompt | llm

def encode_image(image_file):
        return base64.b64encode(image_file.read()).decode()

st.title("Diet Analysis using Gemini")

col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("Upload your image", type=["jpg", "png"], key=1)

with col2:
    if uploaded_file is not None:
        st.image(uploaded_file)
    else:
        st.write("Image Preview")

col3, col4 = st.columns(2)

with col3:
    uploaded_file_1 = st.file_uploader("Upload your image", type=["jpg", "png"], key=2)

with col4:
    if uploaded_file_1 is not None:
        st.image(uploaded_file_1)
    else:
        st.write("Image Preview")

question = st.text_input("Enter a question")

if uploaded_file is not None and question:
    try:
        # Encode the uploaded image to base64
        image = encode_image(uploaded_file)
        
        # Prepare the input for the chain
        input_data = {
            "image": image           # Base64-encoded image
        }
        
        # Call the chain to generate a response
        res = chain.invoke(input_data)
        
        # Display the chatbot's response
        st.write("### Diet Suggestions:")
        st.write(res.content)

    except Exception as e:
        st.error(f"An error occurred: {e}")
