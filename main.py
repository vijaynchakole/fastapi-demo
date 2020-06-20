# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 13:07:58 2020

@author: vijaynchakole

"""
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def hello():
    return{"message" : "hello world"}

@app.get("/items/{item_id}")
def read_item(item_id : int, q : str = None):
    return {"item_id" : item_id, "q" : q}
