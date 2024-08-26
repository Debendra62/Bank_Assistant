from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
from database import vector_store
from langchain_core.runnables import RunnableMap
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-pro', temperature=0)

def general_func(context_query):
    template1 = """
    You are a smart assistant tasked to assist the user based on the given context.
    The user's previous messages are provided as the context.
    Respond to the user's latest query in a way that makes sense based on the entire conversation.
    
    Query: `{query}`
    Context: ```{context}```
    Only provide the response from the provided context.
    """
    prompt_template = PromptTemplate.from_template(template1)
    
    general_chain = RunnableMap(
        {
            "context": lambda x: vector_store.similarity_search(x['context'], k=10),
            "query": lambda x: x['query']
        }
    ) | prompt_template | model | StrOutputParser()

    response = general_chain.invoke({"context": context_query, "query": context_query})
    return response
