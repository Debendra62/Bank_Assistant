from fastapi import FastAPI
import uvicorn
from process_query import process_query

app = FastAPI()

@app.get("/test")
def output(query: str):
    res = process_query(query)
    return {"response": res}

if __name__ == "__main__":
    uvicorn.run(app=app, host="127.0.0.1", port=5556)
