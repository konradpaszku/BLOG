"""Adress Urls for users app"""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    #Default adress URL
    path('', include('django.contrib.auth.urls')),
    # page for register
    path('register/', views.register, name='register'),
]