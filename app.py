import os
from fastapi import FastAPI
from txtgen import test
import sys
sys.path.append('./txtgen')

app = FastAPI()
@app.get("/")
def generate_buzz():
    page = '<html><body><h1>'
    page += test.main()
    page += '</h1></body></html>'
    return page