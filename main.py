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