import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os

import os
from dotenv import load_dotenv
load_dotenv()

## Langsmith Tracking
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")
if langchain_api_key:
    os.environ["LANGCHAIN_API_KEY"] = langchain_api_key
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A Chatbot With OPENAI"


## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant . Please response to the user queries"),
        ("user","Question:{question}")
    ]
)
def generate_response(question,api_key,engine):
    openai.api_key=api_key

    llm=ChatOpenAI(model=engine, api_key=api_key)
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({'question':question})
    return answer

## #Title of the app
st.title("Enhanced Q&A Chatbot With OpenAI")


## Sidebar for settings
st.sidebar.title("Settings")
api_key=st.sidebar.text_input("Enter your Open AI API Key:",type="password")

## Select the OpenAI model
engine=st.sidebar.selectbox("Select Open AI model",["gpt-4o","gpt-4-turbo","gpt-4"])

## MAin interface for user input
st.write("Go ahead and ask any question")
user_input=st.text_input("You:")

if user_input and api_key:
    response=generate_response(user_input,api_key,engine)
    st.write(response)

elif user_input:
    st.warning("Please enter the OpenAI API Key in the sidebar")
else:
    st.write("Please provide the user input")


