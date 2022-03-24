from django.shortcuts import render

# Code has been used from the Code Institute Boutique Ado
# Walkthrough project

def view_basket(request):
    """ A view that renders the basket contents page """

    return render(request, 'basket/basket.html')
