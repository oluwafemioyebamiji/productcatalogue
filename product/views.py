from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, Manufacturer

def productlist(request):
    products = Product.objects.all()#[1:2]
    data = {"Products": list(products.values())} #"pk","name","price"
    response = JsonResponse(data)
    return response

def productdetails(request,pk):
    try:
        product = Product.objects.get(pk = pk)
        data = {"Product": {
            "Name": product.name,
            "Price": product.price,
            "Shipping Cost": product.shippingcost,
            "Quantity": product.quantity,
            "Manufacturer": product.manufacturer.name
        }}
        response = JsonResponse(data)
    except Product.DoesNotExist:
        response = JsonResponse({"Error":{"Code": 404,
        "Message": "Product Not Found"}},
        status=404)

    return response

def manufacturerlist(request):
    manufacturers = Manufacturer.objects.all()#[1:2]
    data = {"Products": list(manufacturers.values())} #"pk","name","price"
    response = JsonResponse(data)
    return response

def manufacturerdetails(request,pk):
    try:
        manufacturer = Manufacturer.objects.get(pk = pk)
        data = {"Product": {
            "Name": manufacturer.name,
            "Location": manufacturer.location
        }}
        response = JsonResponse(data)
    except Manufacturer.DoesNotExist:
        response = JsonResponse({"Error":{"Code": 404,
        "Message": "Manufacturer Not Found"}},
        status=404)
        
    return response