from . import views
from django.urls import path


name = 'profiles_urls'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('fav/<int:id>/', views.favourite_add, name='favourite_add'),
    path('profile/favourites/', views.favourites, name='favourites'),
]
