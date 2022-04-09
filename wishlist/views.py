from django.shortcuts import render, redirect, get_object_or_404
from profiles.models import UserProfile
from products.models import Product
from .models import WishList
from django.contrib.auth.decorators import login_required

@login_required
def wishlist(request):
    """A view to show the user their wishlist"""
    wishes = WishList.objects.filter(user_profile=request.user)
    context = {
        'wishes': wishes,
    }
    return render(request, 'wishlist/wishlist.html', context)

@login_required
def add_to_wishlist(request, product_id):
    user = UserProfile.objects.get()
    product = get_object_or_404(Product, pk=product_id)
    wish = WishList.objects.create(
        user_profile=request.user,
        product=product,
    )

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)