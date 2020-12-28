from django.urls import path
from .views import productlist, productdetails, manufacturerdetails, manufacturerlist
urlpatterns = [
    path('products/', productlist, name="productlist"),
    path('products/<int:pk>/', productdetails, name="productdetails"),
    path('manufacturers/', manufacturerlist, name="manufacturerlist"),
    path('manufacturers/<int:pk>/', manufacturerdetails, name="manufacturerdetails"),
]