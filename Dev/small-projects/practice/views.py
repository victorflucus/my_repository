import datetime

from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse

from practice.models import Project, ProjectIdeas
from practice.forms import AddNewProject


# Create your views here.


# View redirects to page depending on user's selection
def redirector(request, pk):
    project = Project.objects.get(pk=pk)
    site_name = project.title
    return redirect(reverse(f"practice:{site_name}"))


def all_sites(request):
    # query my project model to return all site objects
    projects = Project.objects.all()
    # return a rendered template with the site information passed into it
    return render(request, 'practice/all_sites.html', {'projects': projects})


def clickToAddItems(request):
    return render(request, 'practice/clickToAddItems.html')


def displayEvens(request):
    return render(request, 'practice/displayEvens.html')


def displayMousePosition(request):
    return render(request, 'practice/displayMousePosition.html')


def luckySevens(request):
    return render(request, 'practice/luckySevens.html')

def projectIdeas(request):
    return render(request, 'practice/projectIdeas.html')


def addNewProject(request):
    project_idea = ProjectIdeas()
    # If this is a POST request then process Form data:
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = AddNewProject(request.POST)

        # Check whether form is valid:
        if form.is_valid():
            # write form.cleaned_data to the appropriate project_idea fields
            project_idea.title = form.cleaned_data['title']
            print (project_idea.title)
            project_idea.details = form.cleaned_data['details']
            print(project_idea.details)
            project_idea.due_date = form.cleaned_data['due_date']
            print(project_idea.due_date)
            project_idea.estimated_hours = form.cleaned_data['estimated_hours']
            print(project_idea.estimated_hours)
            project_idea.save()
            # Redirect to complete page

            #return render(request, 'practice/projectIdeas.html')
            return redirect(reverse(f"practice:projectIdeas"))
    # If this is a GET (or any other method) create default form
    else:
        title = ''
        details = ''
        due_date = datetime.date.today()
        estimated_hours = float(24)

        form = AddNewProject(initial={
            'title': title,
            'details': details,
            'due_date': due_date,
            'estimated_hours': estimated_hours,
        })

        context = {
            'form': form,
            'project_idea': project_idea,
        }
        return render(request, 'practice/addNewProject.html', context)

