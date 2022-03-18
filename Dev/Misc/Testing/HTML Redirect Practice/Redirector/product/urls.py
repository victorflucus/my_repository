# product.urls.py
from django.urls import path
from product import views 

urlpatterns = [
    path('details/<str:product_id>/', views.details, name='product-details'),

    path('redirect_by_model/<str:product_id>/', views.redirect_by_model),
    path('redirect_by_name/<str:product_id>/', views.redirect_by_name),
    path('redirect_by_view/<str:product_id>/', views.redirect_by_view),
    path('redirect_by_url/<str:product_id>/', views.redirect_by_url),
]
