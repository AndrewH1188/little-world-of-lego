from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from profiles.models import UserProfile
from products.models import Product
from .models import WishList

# Code has been used from the Code Institute Boutique Ado
# Walkthrough project


def view_wishlist(request):
    """ View the wish list """
    return render(request, 'wishlist/wishlist.html')


def add_to_wishlist(request, item_id):
    """ Add item to the wish list """
    product = Product.objects.get(id=item_id)
    return render(request, 'wishlist/wishlist.html')
