"""Definiuje stronę głowną"""

from django.urls import path

from . import views

app_name = 'blogs'

urlpatterns = [
    #strona głowna.
    path('', views.index, name='index'),
    #dodanie postów
    path('new_post/', views.new_post, name='new_post'),
    #opis postów
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #edycja postów
    path('post/<int:pk>/edit/', views.edit_post, name='edit_post'),
]