from . import views
from django.urls import path


name = 'profiles_urls'

urlpatterns = [
    path('profiles/profile/', views.profile, name='profile'),
    path('profiles/fav/<int:id>/', views.favourite_add, name='favourite_add'),
    path('profiles/favourites/', views.favourites, name='favourites'),
]
