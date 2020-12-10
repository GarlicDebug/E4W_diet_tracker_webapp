from django.views.generic import TemplateView, ListView
import pandas as pd
import requests
from search.models import Product
from search.models import Compare

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    template_name = 'search_results.html'
    model = Product
    model1 = Compare

    def get_queryset(self):
        query = self.request.GET.get('searchValue')
        df = getResults(query)
        df = df.to_dict()

        model_instances = [Product(
            product_nutrient=df['Nutrient'][count],
            product_amount=df['Amount'][count],
            product_unit=df['Unit'][count],
        ) for count in range(len(df['Nutrient']))]

        return model_instances
    #make a function to get a string.


class CompareResultsView(ListView):
    template_name = 'compare_results.html'
    model = Product
    model1 = Compare

    def get_queryset(self):
        query = self.request.GET.get('compareValue1')
        query2 = self.request.GET.get('compareValue2')
        df2 = getResults(query2)
        df2 = df2.to_dict()
        model_compare = [Compare(
            product_nutrient=df2['Nutrient'][count],
            product_amount=df2['Amount'][count],
            product_unit=df2['Unit'][count],
        ) for count in range(len(df2['Nutrient']))]

        df = getResults(query)
        df = df.to_dict()
        model_instances = [Product(
            product_nutrient=df['Nutrient'][count],
            product_amount=df['Amount'][count],
            product_unit=df['Unit'][count],
        ) for count in range(len(df['Nutrient']))]

        return model_instances, model_compare


def getResults(searchTerm):
    #Get the food nutrition database here and pass to views.py
    searchValueinList = searchTerm.split()
    ###VERY IMPORTANT!!! API FOR GETTING DATABASE FROM WEBSITE IS
    ###I2qpT9BiYjXAbynCBVRHV9X5XsWbHi6eQtHIgC1b

    #Below finds the fdcId needed
    errordb = pd.DataFrame({"Nutrient": ["Error"],
                            "Amount": ["Retype again"],
                            "Unit": ["Input Invalid"],})
    fdcId = ""
    if len(searchValueinList) == 1:
        fdcId = requests.get(f"https://api.nal.usda.gov/fdc/v1/foods/search?query={searchValueinList[0]}&pageSize=1&api_key=I2qpT9BiYjXAbynCBVRHV9X5XsWbHi6eQtHIgC1b")
        if fdcId.status_code == 400:
            return errordb

    else:
        quickstr = ""
        for x in range(len(searchValueinList)):
            quickstr += searchValueinList[0] + "%20"
        quickstr = quickstr[:-3]
        fdcId = requests.get(f"https://api.nal.usda.gov/fdc/v1/foods/search?query={quickstr}&pageSize=1&api_key=I2qpT9BiYjXAbynCBVRHV9X5XsWbHi6eQtHIgC1b")

    #fdcId = requests.get("https://api.nal.usda.gov/fdc/v1/foods/search?query=cheddar%20cheese&pageSize=1&api_key=I2qpT9BiYjXAbynCBVRHV9X5XsWbHi6eQtHIgC1b")
    fdcId_dict = fdcId.json()
    try:
        fdcId_dict['foods'][0]
    except IndexError:
        return errordb
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
                'Unit': col3,
    })
    dffinal = dffinal.sort_values(by='Nutrient')
    dffinal = dffinal[dffinal['Nutrient'].str[0].str.isalpha()].reset_index(drop=True)
    return dffinal



