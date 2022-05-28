# -*- coding: utf-8 -*-
"""
Created on Fri May 27 11:33:00 2022

@author: Administrador
"""


import pandas as pd
from datetime import datetime




#asking by time image
range_date = pd.date_range(end = datetime.today(), periods = 100)
#convert pandas datetime to string column
range_string = range_date.strftime('%Y-%m-%d')

# #creating a class to process the call by date
# response = requests.get("https://api.nasa.gov/planetary/apod?api_key=0VdyL4qzq2P4OfTFJTV30pjKOOEj5HLjvf81QwBz")
# new_response = requests.get(jprint(response.json()),
#                             data = {'date':range_s tring[0]})