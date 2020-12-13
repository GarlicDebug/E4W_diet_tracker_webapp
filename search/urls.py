from django.urls import path, include
from .views import HomePageView, SearchResultsView, CompareResultsView
from django.contrib import admin
#from search.views import displayDF

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', HomePageView.as_view(), name='home'),
    path('compare/', CompareResultsView.as_view(), name='compare_results'),
    #path('searchquick/', displayDF, name='search_results'),
]