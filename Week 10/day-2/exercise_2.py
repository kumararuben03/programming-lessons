import os
from fastapi import FastAPI, HTTPException, Query
from langchain_mongodb import MongoDBAtlasVectorSearch
from pymongo import MongoClient
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain.llms import GoogleLLM  # Hypothetical LLM class, adjust if needed
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from typing import Dict

# Load environment variables
load_dotenv()

# Retrieve API keys and other environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MONGODB_ATLAS_CLUSTER_URI = os.getenv("MONGODB_ATLAS_CLUSTER_URI")

if not GEMINI_API_KEY or not MONGODB_ATLAS_CLUSTER_URI:
    raise ValueError("GEMINI_API_KEY or MONGODB_ATLAS_CLUSTER_URI environment variable not set.")

# Initialize FastAPI app
app = FastAPI()

# Initialize embeddings
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GEMINI_API_KEY)

# Initialize MongoDB client and vector store
client = MongoClient(MONGODB_ATLAS_CLUSTER_URI)
DB_NAME = "test_db"
COLLECTION_NAME = "test_collection_pdf"
ATLAS_VECTOR_SEARCH_INDEX_NAME = "test-index-pdf"
MONGODB_COLLECTION = client[DB_NAME][COLLECTION_NAME]

vector_store = MongoDBAtlasVectorSearch(
    collection=MONGODB_COLLECTION,
    embedding=embeddings,
    index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME,
    relevance_score_fn="cosine",
)

# Initialize LLM for generating answers
llm = GoogleLLM(api_key=GEMINI_API_KEY, model="models/generative-001")  # Replace with actual LLM initialization

# Set up text splitting parameters
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

# Load and process the PDF document
def load_and_store_pdf():
    try:
        loader = PyPDFLoader('diabetes.pdf')
        docs = loader.load_and_split(text_splitter)
        
        # Add documents to the vector store
        vector_store.add_documents(docs)
        print("Document Added!")

    except FileNotFoundError:
        print("Error: 'diabetes.pdf' file not found. Ensure the file is in the correct path.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run this function once at startup to load and index the PDF
load_and_store_pdf()

@app.get("/question/")
async def get_ai_answer(question: str = Query(..., description="User's question")) -> Dict[str, str]:
    """
    This endpoint takes a user's question, searches the vector store for relevant content,
    and generates an answer based on the most relevant document content and the question.
    """
    try:
        # Generate embeddings for the query
        query_embedding = embeddings.embed_text(question)
        
        # Search the vector store for relevant documents
        search_results = vector_store.similarity_search_by_vector(query_embedding, k=1)  # Retrieve top match
        
        if not search_results:
            return {"response": "No relevant information found in the document."}

        # Get the most relevant document content
        best_match = search_results[0].get("content", "No content found.")
        
        # Use the LLM to generate an answer based on the best match and the question
        prompt = f"Using the following information:\n\n{best_match}\n\nAnswer the question: {question}"
        ai_answer = llm.generate(prompt)  # Adjust to match your LLM's generate method

        return {"response": ai_answer}

    except Exception as e:
        print("Error:", str(e))
        raise HTTPException(status_code=500, detail="An error occurred while processing your request.")

# Clean up MongoDB client on shutdown
@app.on_event("shutdown")
def shutdown_event():
    client.close()
