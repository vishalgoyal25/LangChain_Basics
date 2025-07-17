import os
from dotenv import load_dotenv
load_dotenv()

## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]= os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"]= os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"]= "true"

## Streamlit Framework
import streamlit as st

st.title("Langchain Demo With OLLAMA-Gemma:2b Model")
input_text= st.text_input("Hello, What Question do you have in your mind?")

## Prompt Template
from langchain_core.prompts import ChatPromptTemplate

prompt= ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the question asked"),
        ("user","Question:{question}")
    ]
)

## Ollama-Gemma:2b Model
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser

llm= Ollama(model="gemma:2b")

output_parser= StrOutputParser()

chain= prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({"question": input_text}))