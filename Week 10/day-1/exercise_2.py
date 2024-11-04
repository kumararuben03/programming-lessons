from dotenv import load_dotenv
import os
from fastapi import FastAPI, Query, HTTPException
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers.datetime import DatetimeOutputParser
from langchain_community.document_loaders import WikipediaLoader
from datetime import datetime

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Verify that the API key is loaded
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set. Please check your .env file.")

# Initialize the FastAPI app
app = FastAPI()

# Initialize the Google Generative AI model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=GEMINI_API_KEY)

# Set up the datetime output parser
output_parser = DatetimeOutputParser()

# Define the chat prompt template
chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You always reply to questions only in datetime patterns"),
        ("human", "{request} \n {format_instructions}"),
    ]
)

# Define the FastAPI endpoint
@app.get("/question/")
async def get_datetime_answer(question: str = Query(..., description="User's question")):
    # Use the prompt chain to generate a response from the LLM
    try:
        
        chain = chat_prompt | llm
        ai_msg = chain.invoke({
            "request": question,
            "format_instructions": output_parser.get_format_instructions()
        })

        # Check if ai_msg.content is empty or null
        if ai_msg is None or ai_msg.content is None:
            raise ValueError("The LLM response is empty or null.")

        # Print the raw output for debugging
        print("Raw AI Response:", ai_msg.content)

        # Parse the output to ensure it follows the datetime format
        # formatted_datetime = output_parser.parse(ai_msg.content)

        # Check if parsing returned None or an unexpected result
        # if formatted_datetime is None:
        #     raise ValueError("The LLM response could not be parsed into a datetime format.")

        # Return the response
        return ai_msg.content

    except Exception as e:
        # Handle and log errors, then return a user-friendly error message
        print("Error:", str(e))
        raise HTTPException(status_code=500, detail="An error occurred while processing your request.")
    
@app.get("/question/{wiki_topic}")
async def get_wiki_answer(wiki_topic: str, question: str = Query(..., description="User's question about the topic")):
    try:
        loader = WikipediaLoader(query=wiki_topic, load_max_docs=1)
        context_text = loader.load()[0].page_content

        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are a helpful assistant.",
                ),
                (
                    "human",
                    "Answer this question:\n{question}\n Here is some extra content:\n{context}"
                )
            ]
        )
        chain = prompt | llm
        ai_msg = chain.invoke({
            "question": wiki_topic,
            "context": question
        })

        # Check if ai_msg.content is empty or null
        if ai_msg is None or ai_msg.content is None:
            raise ValueError("The LLM response is empty or null.")

        # Print the raw output for debugging
        print("Raw AI Response:", ai_msg.content)

        # Parse the output to ensure it follows the datetime format
        # formatted_datetime = output_parser.parse(ai_msg.content)

        # Check if parsing returned None or an unexpected result
        # if formatted_datetime is None:
        #     raise ValueError("The LLM response could not be parsed into a datetime format.")

        # Return the response
        return ai_msg.content

    except Exception as e:
        # Handle and log errors, then return a user-friendly error message
        print("Error:", str(e))
        raise HTTPException(status_code=500, detail="An error occurred while processing your request.")
        