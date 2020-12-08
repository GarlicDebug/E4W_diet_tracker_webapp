from django.db import models
import cgi
import os
import requests
import csv
import json
import pandas as pd
import numpy as np
import re

class Product(models.Model):
    product_name = models.TextField()
    product_nutrient = models.TextField()
    product_unit = models.TextField()

    def __str__(self):
        return "{} - {} - {}".format(self.product_name, self.product_nutrient, self.product_unit)

"""class GettingNutritionValue(models.Model):
    # Get the food nutrition database here and pass to views.py
    # getting the search value

    form = cgi.FieldStorage()
    searchValue = str(form.getvalue('searchValue'))
    # searchValue = "cheddar cheese"
    searchValueinList = searchValue.split()
    #VERY IMPORTANT!!! API FOR GETTING DATABASE FROM WEBSITE IS
    #I2qpT9BiYjXAbynCBVRHV9X5XsWbHi6eQtHIgC1b

    # Below finds the fdcId needed
    fdcId = ""
    if len(searchValueinList) == 1:
        fdcId = requests.get(
            f"https://api.nal.usda.gov/fdc/v1/foods/search?query={searchValueinList[0]}&pageSize=1&api_key=I2qpT9BiYjXAbynCBVRHV9X5XsWbHi6eQtHIgC1b")
    else:
        quickstr = ""
        for x in range(len(searchValueinList)):
            quickstr += searchValue[0] + "%20"
        quickstr = quickstr[:-3]
        fdcId = requests.get(
            f"https://api.nal.usda.gov/fdc/v1/foods/search?query={quickstr}&pageSize=1&api_key=I2qpT9BiYjXAbynCBVRHV9X5XsWbHi6eQtHIgC1b")

    # fdcId = requests.get("https://api.nal.usda.gov/fdc/v1/foods/search?query=cheddar%20cheese&pageSize=1&api_key=I2qpT9BiYjXAbynCBVRHV9X5XsWbHi6eQtHIgC1b")
    fdcId_dict = fdcId.json()
    fdcID = fdcId_dict['foods'][0]['fdcId']

    # Below uses the fdcId found to search for a product's nutritions
    food = requests.get(
        f"https://api.nal.usda.gov/fdc/v1/food/{fdcID}?api_key=I2qpT9BiYjXAbynCBVRHV9X5XsWbHi6eQtHIgC1b")
    food_dict = food.json()

    # populate class with the dict
    df = pd.DataFrame.from_dict(food_dict['foodNutrients'][0])
    for i in range(1, len(food_dict['foodNutrients'])):
        df = df.append(pd.DataFrame.from_dict(food_dict['foodNutrients'][i]))

    df = df.groupby('id')
    col1 = []
    for n, g in df:
        col1.append(str(g['nutrient']['name']))
    col2 = []
    for n, g in df:
        col2.append(g['nutrient']['number'])
    col3 = []
    for n, g in df:
        col3.append(g['nutrient']['unitName'])

    dffinal = pd.DataFrame({
        'Nutrient': col1,
        'Amount': col2,
        'unit': col3})
    print(dffinal)
    it's from row 44-62 for cheddar cheese"""

""""
#Get the food nutrition database here and pass to views.py
#getting the search value
form = cgi.FieldStorage()
searchValue = str(form.getvalue('searchValue'))
#searchValue = "cheddar cheese"
searchValueinList = searchValue.split()
###VERY IMPORTANT!!! API FOR GETTING DATABASE FROM WEBSITE IS
###I2qpT9BiYjXAbynCBVRHV9X5XsWbHi6eQtHIgC1b

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

df = df.groupby('id')
col1 = []
for n, g in df:
    col1.append(str(g['nutrient']['name']))
col2 = []
for n, g in df:
    col2.append(g['nutrient']['number'])
col3 = []
for n, g in df:
    col3.append(g['nutrient']['unitName'])

dffinal = pd.DataFrame({
            'Nutrient': col1,
            'Amount': col2,
            'unit': col3 })
print(dffinal)
it's from row 44-62 for cheddar cheese"""






