import datetime

from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse

from practice.models import Project, ProjectIdeas, TextCountAnalysisEntries
from practice.forms import AddNewProject, TextCountAnalysis

from practice.textCountAnalysis import analyze


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

def textCountAnalysisResults(request):
    text_data = TextCountAnalysisEntries.objects.all()
    return render(request, 'practice/textCountAnalysisResults.html', {'text_data': text_data})


def textCountAnalysis(request):
    # Initialize model entry
    new_text = TextCountAnalysisEntries()
    # If this is a post request....
    if request.method == 'POST':
        # initialize form with info from POST
        form = TextCountAnalysis(request.POST)
        # If form entries aren't valid, return to user with errors
        if not form.is_valid():
            context = {
                'form': form,
            }
            return render(request, 'practice/addNewProject.html', context)
        # If the entries are valid
        else:
            # write form.cleaned_data to the appropriate model fields and redirect the page
            new_text.title = form.cleaned_data['title']
            new_text.paragraph = form.cleaned_data['paragraph']
            new_text.source = form.cleaned_data['source']
            new_text.save()
            #call text cout analysis function
            result = analyze(new_text.paragraph)
            new_text.frequency_result = result[0]
            new_text.distinct_words_result = result[1]
            new_text.save()
            return redirect(reverse(f"practice:textCountAnalysisResults"))
    # If this is not a post request
    else:
        # Initialize form variables and load fresh form
        title = ''
        paragraph = ''
        source = ''

        form = TextCountAnalysis(initial={
            'title': title,
            'paragraph': paragraph,
            'source': source,
        })

        context = {
            'form': form,
            'new_text': new_text,
        }

        return render(request, 'practice/textCountAnalysis.html', context)

def clickToAddItems(request):
    return render(request, 'practice/clickToAddItems.html')


def displayMousePosition(request):
    return render(request, 'practice/displayMousePosition.html')


def luckySevens(request):
    return render(request, 'practice/luckySevens.html')


def projectIdeas(request):
    project_ideas = ProjectIdeas.objects.all()
    return render(request, 'practice/projectIdeas.html', {'project_ideas': project_ideas})


def addNewProject(request):
    project_idea = ProjectIdeas()
    # If this is a POST request then process Form data:
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = AddNewProject(request.POST)

        # Check whether form is valid:
        # if not, regenerate the form with errors
        if not form.is_valid():
            context = {
                'form': form,
            }
            return render(request, 'practice/addNewProject.html', context)
        # if so....
        else:
            # write form.cleaned_data to the appropriate model fields and redirect the page
            project_idea.title = form.cleaned_data['title']
            project_idea.details = form.cleaned_data['details']
            project_idea.due_date = form.cleaned_data['due_date']
            project_idea.estimated_hours = form.cleaned_data['estimated_hours']
            project_idea.save()
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
