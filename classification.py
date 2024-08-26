
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

import os
from dotenv import load_dotenv
from langchain_core.runnables import RunnableMap
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
model = ChatGoogleGenerativeAI(model = 'gemini-pro', temperature=0)

def classification_query(user_query):

    my_template='''
    You are a smat virtual assistant that will analyze the query given by the user and classify the intent based on the query.
    <Interest Rate>:Questions regarding the interest rate only.
    <Service Charges>:Questions regarding the charges of the services like mobile banking charges, atm card charge, atm transaction charges etc.
    <Location>:Queries related to the location of bank,ATM,branches or branch offices only.
    <Request- Opening/Applying>:Queries from the user about  opening saving account, applying loan, apply credit card, request cheque book etc.
    <Request-Closing>: Queries from the user about the activities regarding closing or blocking like closing account, block cards, cancel cheque, block mobile/internet banking etc.
    <Complaint>: Reflections of an intention to complain or express dissatisfaction, or requests for feedback or complaint forms.
    <Others>: Queries that are out of the above intent.

    **Question Example:**

    **Question**: "What could be the interest rate if i take a loan?"
        **Query**: "What could be the interest rate if i take a loan?"
        **Intent**:
            "type":"interest rate",
            "subject":"Interesr Rate on [subject]"
        
        
    **Question**: "What is the total cost on mobile banking?"
        **Query**: "What is the total cost on mobile banking?"
        **Intent**:
            "type":"Service Charges",
            "subject":"Charges on [subject]"
        

    **Question**: "Where is the location of the bank?"
        **Query**: "Is there any ATM nearby?"
        **Intent**:
            "Intent":"Location",
            "subject":"Location about [subject]"
        


    **Question**: "I want to block my mobile banking."
        **Query**: "I want to block my mobile banking."
        "Intent":"requesting on closing [subject]"



    **Question**: "The service of mobile banking is too poor."
        **Query**: "The service of mobile banking is too poor."
        "Intent":"complaints",

    In case of user query that is not related with the above intent do the following:
    **Question**: "I am studying now."
        **Query**: "I am studying now."
        **Intent**: "Others"
        
        
    Classify the intent of the question and answer with the Query and Intent along with type and subject.

    '''

    prompt =PromptTemplate.from_template(template= my_template)
    chain = RunnableMap(
    {
        'query': lambda x: x['query'],
    },
) | prompt| model |StrOutputParser()

    response= chain.invoke({"query":user_query})

    return response

