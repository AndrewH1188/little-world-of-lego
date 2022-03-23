from django.urls import path
from . import views

# Code has been used from the Code Institute Boutique Ado
# Walkthrough project

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
]
