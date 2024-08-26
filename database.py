import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import CSVLoader
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
import logging

load_dotenv()
logging.basicConfig(level=logging.INFO)

host = os.getenv('HOST')
port = os.getenv('PORT')

try:
    loader = CSVLoader(r"E:\Projects\Bank_Assistant\dataset\dataset.csv", encoding='unicode_escape')
    docs = loader.load()
    logging.info("Documents loaded successfully.")

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    logging.info("Documents split successfully.")

    embedding_func = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_store = Chroma.from_documents(splits, embedding_func, persist_directory="chroma_store")
    logging.info("Vector store created successfully.")
except Exception as e:
    logging.error(f"An error occurred: {e}")
