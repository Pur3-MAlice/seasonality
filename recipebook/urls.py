from . import views
from django.urls import path

name = 'recipebook_urls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('search_results/', views.search_results, name='search_results'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('rate/<int:recipe_id>/<int:rating>/', views.rate),
]
