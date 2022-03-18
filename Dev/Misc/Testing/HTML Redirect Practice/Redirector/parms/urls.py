# parms.urls.py
from django.urls import path
from django.views.generic.base import RedirectView

from parms import views

urlpatterns = [
    path("show_random_number/", views.show_random_number ),
    path("show_number/", views.show_number, name="show-number"),
]
