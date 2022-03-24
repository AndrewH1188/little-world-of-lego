from django.urls import path
from . import views

# Code has been used from the Code Institute Boutique Ado
# Walkthrough project

urlpatterns = [
    path('', views.view_basket, name='view_basket')
]
