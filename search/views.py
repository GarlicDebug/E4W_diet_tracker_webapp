from django.shortcuts import render
from django.views.generic import TemplateView, ListView
import pandas as pd
import requests
from .models import Product
from django.http import HttpResponse, HttpResponseRedirect

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    template_name = 'search_results.html'
    model = Product
    def get_queryset(self):
        query = self.request.GET.get('searchValue')
        print(query)
        df = getResults(query)
        #df = str(df.to_html())
        return render('search_results.html', {'df': df.to_html()})
    """    
    def get_queryset(self):
        query = self.request.GET.get('searchValue') #HERE IS WHERE WE GET THE VALUE

        dffinal = getResults(query)                  #FROM THE SEARCH BAR

        #dffinal is a dataframe

        #EVERYTHING'S GOOD UPTO HERE
        context = {'table_content': str(dffinal.to_html())}
        df = dffinal.to_html()
        return render('search_results.html', )
        #return render(dffinal.to_html(), 'search_results.html')"""
    """def get_queryset(self):
        query = self.request.GET.get('searchValue')
        query = getResults(query)
        context = {'table_content': query.to_html()}
        return render('search_results.html', context)"""
    """
    def mainview(request):

        query = request.GET.get('searchValue')
        print(query)
        data = getResults(query)
        context = { 'df': data.to_html}
        return render(request, 'templates/search_results.html', context)"""





def getResults(searchTerm):
    #Get the food nutrition database here and pass to views.py
    searchValueinList = searchTerm.split()
    ###VERY IMPORTANT!!! API FOR GETTING DATABASE FROM WEBSITE IS
    ###I2qpT9BiYjXAbynCBVRHV9X5XsWbHi6eQtHIgC1b

    #Below finds the fdcId needed
    fdcId = ""
    if len(searchValueinList) == 1:
        fdcId = requests.get(f"https://api.nal.usda.gov/fdc/v1/foods/search?query={searchValueinList[0]}&pageSize=1&api_key=I2qpT9BiYjXAbynCBVRHV9X5XsWbHi6eQtHIgC1b")
    else:
        quickstr = ""
        for x in range(len(searchValueinList)):
            quickstr += searchValueinList[0] + "%20"
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
                'Unit': col3,
    })
    return dffinal



