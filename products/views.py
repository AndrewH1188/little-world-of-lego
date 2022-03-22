from django.shortcuts import render
from .models import Product

# Code has been used from the Code Institute Boutique Ado
# Walkthrough project

def all_products(request):
    """ A view to show all products, including sorting and search queries """
    
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
