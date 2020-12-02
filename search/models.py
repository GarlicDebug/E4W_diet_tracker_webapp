from django.db import models
import cgi, cgitb
import os
import requests
import csv
import json


# Create your models here.
#Get the food nutrition database here and pass to views.py
#getting the search value
form = cgi.FieldStorage()
searchValue = form.getvalue('searchValue')
#VERY IMPORTANT!!! API FOR GETTING DATABASE FROM WEBSITE IS
#I2qpT9BiYjXAbynCBVRHV9X5XsWbHi6eQtHIgC1b

#Below finds the fdcId needed
fdcId = requests.get("https://api.nal.usda.gov/fdc/v1/foods/search?query=cheddar%20cheese&pageSize=1&api_key=I2qpT9BiYjXAbynCBVRHV9X5XsWbHi6eQtHIgC1b")
fdcId_dict = fdcId.json()
fdcID = fdcId_dict['foods'][0]['fdcId']
print(fdcID)
#Below uses the fdcId found to search for a product's nutritions
food = requests.get(f"https://api.nal.usda.gov/fdc/v1/food/{fdcID}?api_key=I2qpT9BiYjXAbynCBVRHV9X5XsWbHi6eQtHIgC1b")
food_dict = food.json()
print(food_dict)




