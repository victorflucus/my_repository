from django.contrib import admin
from django.urls import path
from projects import views

#Defining variables for path names
app_name = "projects"

urlpatterns = [
    path('', views.all_projects, name='all_projects'),
    #path converter -> passes the number provided in the url to the project detail template within my views
    path('<int:pk>', views.project_detail, name='project_detail'),

]