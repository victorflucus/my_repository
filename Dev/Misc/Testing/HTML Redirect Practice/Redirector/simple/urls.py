# simple.urls.py
from django.urls import path
from simple import views 

urlpatterns = [
    path('handmade/', views.hand_made_redirect),
    path('redirect/', views.redirect_view),
]
