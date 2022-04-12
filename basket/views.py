from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from products.models import Product

# Code has been used from the Code Institute Boutique Ado
# Walkthrough project


def view_basket(request):
    """ A view that renders the basket contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the product selected to our basket """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    # Adds an item if one isn't in our basket or updates the quantity
    # if the same product already exists in our basket
    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(
            request,
            f'Updated {product.name} quantity to {basket[item_id]}')
    else:
        basket[item_id] = quantity
        messages.success(
            request,
            f'{basket[item_id]}x {product.name} was added to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """ Adjust a quantity of the product selected in our basket """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    product = None
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop(item_id)

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """ Remove a product from our basket """

    try:
        product = get_object_or_404(Product, pk=item_id)
        product = None
        if 'product' in request.POST:
            product = request.POST['product']
        basket = request.session.get('basket', {})

        if product:
            del basket[item_id]
            basket.pop(item_id)
        else:
            basket.pop(item_id)

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.success(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
