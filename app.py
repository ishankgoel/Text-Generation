import os
from fastapi import FastAPI
from txtgen.test import main
import sys
sys.path.append('./txtgen')

app = FastAPI()

@app.get("/ping")
def ping():
    
    return {"message":"pong"}

@app.get("/chat")
def generate_buzz():
    page = '<html><body><h1>'
    page += main()
    page += '</h1></body></html>'