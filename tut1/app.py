from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
from dotenv import load_dotenv
import uvicorn
import os

load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY') or ''

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="Parent Server"
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai",
)

model = ChatOpenAI()
prompt = ChatPromptTemplate.from_template("Provide me an essay about {topic}")
prompt1 = ChatPromptTemplate.from_template("Provide me a poem about {topic}")

# Route 1
add_routes(
    app,
    prompt | model,
    path="/essay"
)

# Route 1
add_routes(
    app,
    prompt1 | model,
    path="/poem"
)

# Adding routes as APIs
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)