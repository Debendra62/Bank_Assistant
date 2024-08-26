from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import logging
from database import vector_store
from langchain_core.runnables import RunnableMap
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
logging.basicConfig(level=logging.INFO)

model = ChatGoogleGenerativeAI(model='gemini-pro', temperature=0)

def general_func(user_query):
    template1 = """
    You are a smart assistant tasked with assisting the user based on the provided context.
    The query is provided in double backticks: ``{query}``.
    The context is provided in triple backticks: ```{context}```.
    
    Please provide a concise response based on the context, without repeating the user's query.
    If the context does not contain relevant information, politely state that the information is not available.
    """
    
    prompt_template = PromptTemplate.from_template(template1)
    
    try:
        general_chain = RunnableMap(
            {
                "context": lambda x: vector_store.similarity_search(f"{x['query']}", k=10),
                "query": lambda x: x['query']
            }
        ) | prompt_template | model | StrOutputParser()
        
        response = general_chain.invoke({"query": user_query})
        logging.info("Query processed successfully.")
        return response
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return "Sorry, I couldn't process your request."
