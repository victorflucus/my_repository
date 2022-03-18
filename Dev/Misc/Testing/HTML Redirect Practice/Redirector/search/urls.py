# search.urls.py
from django.urls import path
from django.views.generic.base import RedirectView

from search import views

urlpatterns = [
    path("inline_redirect/<str:term>/", 
        RedirectView.as_view(url="https://google.com/?q=%(term)s")),

    path("inherit_redirect/<str:term>/", views.SearchRedirectView.as_view()),

    path("random_redirect/<str:term>/", views.RandomSearchView.as_view()),
]
