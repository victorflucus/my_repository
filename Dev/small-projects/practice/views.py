from django.shortcuts import render
from practice.models import Project

# Create your views here.

# this is an example view
def project_list(request):
    return render(request, 'practice/index.html')

# Main list of javascript sites
def all_sites(request):
# query my project model to return all site objects
    projects = Project.objects.all()
# return a rendered template with the site information passed into it
    return(render(request, 'projects/all_sites.html', {'projects':projects}))

def site_detail(request, pk):
    # get an object from my product model that matches a specific pk passed in the url
    project = Project.objects.get(pk=pk)
    return(render(request, 'projects/site_detil.html', {'projects':project}))