from django.urls import path
from .views import HomePageView, SearchResultsView
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', HomePageView.as_view(), name='home'),
]