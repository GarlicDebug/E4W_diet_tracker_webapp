from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.db.models import Q
#from .models import FoodResults
class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    #model = ........webscraping results
    template_name = 'search_results.html'
    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = FoodResults.objects.filter(
            Q(fdcId__icontains=query)
        )
        return object_list


