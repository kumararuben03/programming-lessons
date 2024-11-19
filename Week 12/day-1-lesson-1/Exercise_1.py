from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_sql_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=GEMINI_API_KEY)

database_file_path = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(database_file_path)
# os.makedirs(os.path.dirname(database_file_path), exist_ok=True)
df = pd.read_csv("students.csv")
df.to_sql('students', con=engine, if_exists='replace', index=False)

db = SQLDatabase.from_uri(database_file_path)
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

sql_agent = create_sql_agent(
    toolkit=toolkit,
    llm=llm,
    verbose=True,
    allow_dangerous_code=True
)

QUESTION = """Give me the highest math, reading and writing score.
"""

res = sql_agent.invoke(QUESTION)

print(res["output"])