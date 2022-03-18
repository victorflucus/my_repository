# product.views.py
from django.http import HttpResponse
from django.shortcuts import redirect
from product.models import Product

def details(request, product_id):
    product = Product.objects.get(id=product_id)
    return HttpResponse(product.name + '\n', content_type="text/plain")

def redirect_by_model(request, product_id):
    product = Product.objects.get(id=product_id)
    return redirect(product)

def redirect_by_name(request, product_id):
    return redirect("product-details", product_id)

def redirect_by_view(request, product_id):
    return redirect(details, product_id)

def redirect_by_url(request, product_id):
    return redirect("/details/%s/" % product_id)
