# destination.urls.py
from django.urls import path

from destination import views

urlpatterns = [
    path('hello/', views.hello_world),
    path('destination/', views.destination),
]
