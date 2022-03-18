# Redirector/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('destination.urls')),
    path('', include('simple.urls')),
    path('', include('product.urls')),
    path('', include('search.urls')),
    path('', include('parms.urls')),
]
