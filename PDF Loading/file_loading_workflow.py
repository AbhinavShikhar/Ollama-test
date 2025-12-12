from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_chroma import Chroma
import os

# Important Variables
PDF_PATH = "/workspaces/Example-LangChain-Repository/Understanding Modelfile in Ollama.pdf"
DB_DIR = "./sql_chrome.db"
MODEL_NAME = "test-llm"

# Setting up variables in my chain
model = ChatOllama(model=MODEL_NAME)
prompt = ChatPromptTemplate.from_template(
    """ You are an AI assistant. Use ONLY the provided context to answer the question. If the answewr is not clearly and directed supported by the context, respond exactly with: 
     "I don't have enough context to answer that"
    DO NOT make up facts or speculate.
    "You must base your answers ONLY on the provided context.
    If you include any information, you must reference the filename and the page it came from.
    If there is no relevant context, respond: 'I don't have enough context to answer that'
    """