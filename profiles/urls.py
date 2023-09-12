from . import views
from django.urls import path


# name of url.py
name = 'profiles_urls'


# Profile URL patterns
urlpatterns = [
    path('profiles/profile/', views.profile, name='profile'),
    path('profiles/fav/<int:id>/', views.favourite_add, name='favourite_add'),
    path('profiles/favourites/', views.favourites, name='favourites'),
]
