from fastapi import FastAPI
from socket import gethostname
app = FastAPI()
@app.get("/")
def read_root():
    return {"host": gethostname()}