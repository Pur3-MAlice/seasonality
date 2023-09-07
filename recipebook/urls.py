from . import views
from django.urls import path

name = 'recipebook_urls'

urlpatterns = [
    path('', views.RecipeList.as_view(), name="home"),
    path('search_results/<int:page>/', views.search_results, name='search_results'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
]
