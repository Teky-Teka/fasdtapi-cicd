from typing import Union
from fastapi import FastAPI
app = fastAPI()

@app.get('/')
def read_root():
    return {"Hello,":  "World!"}
