from general_chain import general_func
from classification import classification_query
import logging

logging.basicConfig(level=logging.INFO)

def process_query(query):
    try:
        intent = classification_query(query)
        
        if intent in ['Location', '<Location>']:
            logging.info(f"Location intent detected: {intent}")
            return "The bank is located in Basundhara."
        
        result = general_func(query)
        return result
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return "Sorry, I couldn't process your request."
