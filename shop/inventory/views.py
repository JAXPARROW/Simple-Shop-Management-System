from django.shortcuts import render
from django.http import HttpResponse
from inventory.models import Product

def index(request):
    template = "inventory/index.html"
    product_list = Product.objects.all()
    context = {'product_list': product_list}
    return render(request, template, context)
    