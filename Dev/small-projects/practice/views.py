from django.shortcuts import render, redirect

from django.urls import reverse

from practice.models import Project


# Create your views here.


#View redirects to page depending on user's selection
def redirector(request, pk):
    project = Project.objects.get(pk=pk)
    site_name = project.title
    return redirect(reverse(f"practice:{site_name}"))

def all_sites(request):
# query my project model to return all site objects
    projects = Project.objects.all()
# return a rendered template with the site information passed into it
    return render(request, 'practice/all_sites.html', {'projects':projects})

def clickToAddItems(request):
    return render(request, 'practice/clickToAddItems.html')

def displayEvens(request):
    return render(request, 'practice/displayEvens.html')

def displayMousePosition(request):
    return render(request, 'practice/displayMousePosition.html')

def luckySevens(request):
    return render(request, 'practice/luckySevens.html')


