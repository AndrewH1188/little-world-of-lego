from django.urls import path
from . import views

# Code has been used from the Code Institute Boutique Ado
# Walkthrough project

urlpatterns = [
    path('', views.view_wishlist, name='view_wishlist'),
    path('add_to_wishlist', views.add_to_wishlist, name='add_to_wishlist'),
]
