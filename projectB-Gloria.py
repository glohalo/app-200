# -*- coding: utf-8 -*-
"""
Created on Thu May 26 11:43:35 2022

@author: Gloria
"""

import urllib.request, urllib.parse, urllib.error
import json
import ssl


response = urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=0VdyL4qzq2P4OfTFJTV30pjKOOEj5HLjvf81QwBz')
print('RESPONSE:', response)

print(response.data.decode("utf-8"))

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = '0VdyL4qzq2P4OfTFJTV30pjKOOEj5HLjvf81QwBz'
    serviceurl = 'https://api.nasa.gov/planetary/apod?api_key=0VdyL4qzq2P4OfTFJTV30pjKOOEj5HLjvf81QwBz'
else :
    serviceurl = 'https://api.nasa.gov/planetary/apod'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    Date = input('Enter Date: ')
    if len(Date) < 1: break

    parms = dict()
    parms['date'] = Date
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    Astronomy_Picture_of_the_Day = js['explanation'][0]['hdurl']['title']['url']
    print('lat', Astronomy_Picture_of_the_Day )
    img = js['explanation'][0]['date']
    print(img)

# Code: http://www.py4e.com/code3/geojson.py