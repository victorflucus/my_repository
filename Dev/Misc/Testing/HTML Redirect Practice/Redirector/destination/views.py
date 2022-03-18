# destination.views.py
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello World\n", content_type='text/plain')

def destination(request):
    return HttpResponse("You were redirected\n", content_type='text/plain')
