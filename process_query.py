from general_chain import general_func
from classification import classification_query

# Memory to keep track of previous queries and responses
memory = []

def process_query(query):
    global memory

    # Check if the intent is specific
    intent = classification_query(query)
    if intent in ['Location', '<Location>']:
        print(f"The intent is ============>", intent)
    
    # Add the current query to memory
    memory.append({"query": query})
    
    # Combine the previous memory context with the current query
    context = ' '.join([item["query"] for item in memory])
    
    # Generate a response based on the combined context
    result = general_func(context)
    
    # Store the result in memory
    memory[-1]["response"] = result
    
    return result
