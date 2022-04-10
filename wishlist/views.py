from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile
from products.models import Product
from .models import WishList

# Code has been used from the Code Institute Boutique Ado
# Walkthrough project

def view_wishlist(request):

    return render(request, 'wishlist/wishlist.html')

def add_to_wishlist(request):
    product = get_object_or_404(Product, pk=item_id)
    request.session['view_wishlist'] = wishlist
    return redirect(redirect_url)