from django.urls import path
from board import views

urlpatterns = [
    #127.0.0.1:8000/board/
    path('', views.index),
]