from fastapi import FastAPI, HTTPException
import uvicorn
from process_query import process_query
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)

@app.get("/test")
def output(query: str):
    try:
        res = process_query(query)
        return {"response": res}
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

if __name__ == "__main__":
    uvicorn.run(app=app, host="127.0.0.1", port=5556)
