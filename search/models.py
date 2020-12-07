from django.db import models
import cgi, cgitb
import os
import requests
import csv
import json
import pandas as pd
import re


#Get the food nutrition database here and pass to views.py
#getting the search value
form = cgi.FieldStorage()
#searchValue = str(form.getvalue('searchValue'))
searchValue = "cheddar cheese"
searchValueinList = searchValue.split()
#VERY IMPORTANT!!! API FOR GETTING DATABASE FROM WEBSITE IS
#I2qpT9BiYjXAbynCBVRHV9X5XsWbHi6eQtHIgC1b

#Below finds the fdcId needed
fdcId = ""
if len(searchValueinList) == 1:
    fdcId = requests.get(f"https://api.nal.usda.gov/fdc/v1/foods/search?query={searchValueinList[0]}&pageSize=1&api_key=I2qpT9BiYjXAbynCBVRHV9X5XsWbHi6eQtHIgC1b")
else:
    quickstr = ""
    for x in range(len(searchValueinList)):
        quickstr += searchValue[0] + "%20"
    quickstr = quickstr[:-3]
    fdcId = requests.get(f"https://api.nal.usda.gov/fdc/v1/foods/search?query={quickstr}&pageSize=1&api_key=I2qpT9BiYjXAbynCBVRHV9X5XsWbHi6eQtHIgC1b")

#fdcId = requests.get("https://api.nal.usda.gov/fdc/v1/foods/search?query=cheddar%20cheese&pageSize=1&api_key=I2qpT9BiYjXAbynCBVRHV9X5XsWbHi6eQtHIgC1b")
fdcId_dict = fdcId.json()
fdcID = fdcId_dict['foods'][0]['fdcId']

#Below uses the fdcId found to search for a product's nutritions
food = requests.get(f"https://api.nal.usda.gov/fdc/v1/food/{fdcID}?api_key=I2qpT9BiYjXAbynCBVRHV9X5XsWbHi6eQtHIgC1b")
food_dict = food.json()

#populate class with the dict
df = pd.DataFrame.from_dict(food_dict['foodNutrients'][0])
for i in range(1, len(food_dict['foodNutrients'])):
    df = df.append(pd.DataFrame.from_dict(food_dict['foodNutrients'][i]))


dfgroup = df.groupby('id')
row1 = []
for n, g in dfgroup:
    row1.append(str(g['nutrient']['name']))
row2 = []
for n, g in dfgroup:
    row2.append(g['nutrient']['number'])
row3 = []
for n, g in dfgroup:
    row3.append(g['nutrient']['unitName'])

dffinal = pd.DataFrame({
            'Nutrient': row1,
            'Amount': row2,
            'unit': row3 })
print(dffinal)






