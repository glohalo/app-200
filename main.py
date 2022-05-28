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


@app.get("/apod-planetary")
async def planetary():
    raw_response = requests.get(url)
    response = json.loads(raw_response.text)
    json_response = raw_response.json()
    return json_response

@app.get("/apod/count")
async def planetary():
    params = {'start_date': '2022-03-28', 'end_date':'2022-05-28'}
    raw_response = requests.get(url, params=params)
    json_response = raw_response.json()
    return json_response
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
async def planetary(page_num: int = 1, page_size: int = 10):
    start = (page_num - 1)*page_size
    end = start + page_size
    params = {'start_date': '2022-02-17', 'end_date':'2022-03-30'}
    raw_response = requests.get(url, params=params)
    json_response = raw_response.json()
    data_length = len(json_response)
    
    response = {
            "json_response": json_response[start:end],
            "total": data_length,
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



# #connection
# response = requests.get("https://api.nasa.gov/planetary/apod?api_key=0VdyL4qzq2P4OfTFJTV30pjKOOEj5HLjvf81QwBz")
# #check if conection is ok
# print(response.status_code)  #shows 200, all is ok 

# #Part 2. Readding the data
# print(response.json())
# #creating a formatted string of the Python JSON object
# def jprint(obj):
#     text = json.dumps(obj, sort_keys=True, indent=4)
#     print(text)
        
# print(jprint(response.json()))
# #I have to call 110 data image
# jprint(response.json()['date']['@attr'])

# #asking by time image
# range_date = pd.date_range(end = datetime.today(), periods = 100)
# #convert pandas datetime to string column
# range_string = range_date.strftime('%Y-%m-%d')
