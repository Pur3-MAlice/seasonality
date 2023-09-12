from . import views
from django.urls import path


# name of url.py
name = 'recipebook_urls'


# Recipebook URL patterns. Formatted for python
urlpatterns = [
    path(
        '',
        views.IndexView.as_view(),
        name='home'),
    path(
        'recipebook/add_recipe/',
        views.add_recipe,
        name="add_recipe"),
    path(
        'recipebook/update_recipe/<recipe_id>/',
        views.update_recipe,
        name="update_recipe"),
    path(
        'recipebook/delete_recipe/<recipe_id>/',
        views.delete_recipe,
        name='delete_recipe'),
    path(
        'recipebook/search_results/',
        views.search_results,
        name='search_results'),
    path(
        'recipebook/<slug:slug>/',
        views.RecipeDetail.as_view(),
        name='recipe_detail'),
    path(
        'rate/<int:recipe_id>/<int:rating>/',
        views.rate),
]
