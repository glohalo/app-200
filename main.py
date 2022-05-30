# -*- coding: utf-8 -*-1
"""
Created on Fri May 27 11:33:00 2022

@author: Gloria
"""

import requests
import json
from fastapi import FastAPI
from typing import Union
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


url = 'https://api.nasa.gov/planetary/apod?api_key=0VdyL4qzq2P4OfTFJTV30pjKOOEj5HLjvf81QwBz'
@app.get("/")
async def root():
    return {"Message": "Hello World"}


{
  "json_response" : [...],
  "pagination": {
      "next": "link to the next page",
      "previous": "link to the previous page",
      },
  "count": "total number of items",
  "total": "total number of pages"
 }

@app.get("/Query-pagination")
async def astronomy(page_num: int = 1, page_size: int = 10):
    start = (page_num - 1)*page_size
    end = start + page_size
    params = {'start_date': '2022-02-19', 'end_date':'2022-05-30', 'hd':True}
    raw_response = requests.get(url, params=params)
    json_response = raw_response.json()
  
    list_response = []
    for x in json_response:
        element = {}
        if 'hdurl' in x:
            element['hdurl'] = x['hdurl']
        element['explanation'] = x['explanation']
        element['title'] = x['title']
        element['url'] = x['url']
        list_response.append(element)
        

    json_response = list_response
    data_length = len(json_response)
    
    #building pagination
    response = {
            "json_response": json_response[start:end],
            "total": data_length - 1,
            "count": page_size,
            "pagination":{},
            }
    if end >= data_length:
        response["pagination"]["next"] = None
        if page_num > 1:
            response["pagination"]["pagination"] = f"/posts?page_num={page_num-1}&page_size={page_size}"
        else:
            response["pagination"]["previous"] = None
    else:
        if page_num > 1:
            response["pagination"]["previous"] = f"/posts?page_num={page_num-1}&page_size={page_size}"
        else:
            response["pagination"]["previous"] = None
        
        response["pagination"]["pagination"] = f"/posts?page_num={page_num+1}&page_size={page_size}"
        
        return response


