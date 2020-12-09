from django.urls import path, include
from .views import HomePageView, SearchResultsView
from django.contrib import admin
#from search.views import displayDF

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', HomePageView.as_view(), name='home'),
    #path('searchquick/', displayDF, name='search_results'),
]