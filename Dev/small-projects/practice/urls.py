"""practice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from practice import views

app_name = "practice"
urlpatterns = [
    path('', views.all_sites, name='all_sites'),
    path('<int:pk>', views.redirector, name='redirector'),
    path('clickToAddItems', views.clickToAddItems, name='clickToAddItems'),
    path('displayEvens', views.displayEvens, name='displayEvens'),
    path('displayMousePosition', views.displayMousePosition, name='displayMousePosition'),
    path('luckySevens', views.luckySevens, name='luckySevens'),
    path('addNewProject', views.addNewProject, name='addNewProject'),
]
