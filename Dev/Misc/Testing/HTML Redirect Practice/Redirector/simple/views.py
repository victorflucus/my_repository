# simple.views.py
from django.http import HttpResponse
from django.shortcuts import redirect

def hand_made_redirect(request):
    response = HttpResponse(status=302)
    response['Location'] = '/destination/'
    return response

def redirect_view(request):
    return redirect('/destination/')
