from django import template
# Code has been used from the Code Institute Boutique Ado
# Walkthrough project

register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
