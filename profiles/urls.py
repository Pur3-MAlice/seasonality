from . import views
from django.urls import path


name = 'profiles_urls'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
]