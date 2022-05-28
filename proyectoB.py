# -*- coding: utf-8 -*-
"""
Created on Thu May 26 14:06:33 2022

@author: Administrador
"""

#pip install flask-restful 
pip install request

from urllib import request
from urllib import parse
import json
from flask import Flask
from flask_restful import Resource, Api

#general info
response = request.urlopen('https://api.nasa.gov/planetary/apod?api_key=0VdyL4qzq2P4OfTFJTV30pjKOOEj5HLjvf81QwBz')
print('RESPONSE:', response)
print('URL     :', response.geturl())
respose = response.geturl()
#get the status
print(response.status_code)
#read it in json
print(response.json())

headers = response.info()
print('DATE    :', headers['date'])
print('HEADERS :')
print('---------')
print(headers)

data = response.read().decode('utf-8')
print('LENGTH  :', len(data))
print('DATA    :')
print('---------')
print(data)


js = json.loads(data)
print('Items:', len(js))

for item in js:
    print(item)
    
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())
print(item['explanation'])
    print(hdurl', item['hdurl'])
    print('title', item['title'])
    print('url', item['url'])
