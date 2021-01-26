import os
from fastapi import FastAPI
from test import main
import sys
sys.path.append('./txtgen')

app = FastAPI()

@app.get("/")
def start():
    
    return {"message":"Hi There visitor. Go to /ping & /chat"}

@app.get("/ping")
def ping():
    
    return {"message":"pong"}

@app.get("/chat")
def generate_buzz():
    page = '<html><body><h1>'
    page += main()
    page += '</h1></body></html>'
    return page