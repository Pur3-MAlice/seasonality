from . import views
from django.urls import path

name = 'recipebook_urls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('add_recipe/', views.add_recipe, name="add_recipe"),
    path('update_recipe/<recipe_id>/', views.update_recipe, name="update_recipe"),
    path('delete_recipe/<recipe_id>/', views.delete_recipe, name='delete_recipe'),
    path('delete_comment/<comment_id>/', views.delete_comment, name='delete_comment'),
    path('search_results/', views.search_results, name='search_results'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('rate/<int:recipe_id>/<int:rating>/', views.rate),
]
