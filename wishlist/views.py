from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
# from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile
from products.models import Product
from .models import WishList
# from .models import Order, OrderLineItem


# Code has been used from the Code Institute Boutique Ado
# Walkthrough project

def view_wishlist(request):
    """ View the wish list """
    return render(request, 'wishlist/wishlist.html')


def add_to_wishlist(request, item_id):
    """ Add item to the wish list """
    product = Product.objects.get(id=item_id)
    # order_line_item = OrderLineItem(
    #     order=order,
    #     product=product,
    # )
    # order_line_item.save()
    
    return render(request, 'wishlist/wishlist.html')
    