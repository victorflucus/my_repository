# parms.views.py
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from random import choice
from urllib.parse import urlencode

def show_random_number(request):
    data = { "number":choice([1, 2, 3, 4, 5]), }

    base_url = reverse("show-number")
    query_string = urlencode(data)
    url = f"{base_url}?{query_string}"
    return redirect(url)

def show_number(request):
    number = request.GET.get("number", 0)
    return HttpResponse("Number=%s\n" % number, content_type="text/plain")
