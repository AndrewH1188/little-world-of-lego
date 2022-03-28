from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Code has been used from the Code Institute Boutique Ado
# Walkthrough project

def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "You don't have any items in your basket at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)