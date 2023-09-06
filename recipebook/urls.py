from . import views
from django.urls import path

name = 'recipebook_urls'

urlpatterns = [
    path('', views.RecipeList.as_view(), name="home"),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('search_results/', views.SearchResults, name='search_results'),
]
