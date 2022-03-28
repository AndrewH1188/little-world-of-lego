from django.urls import path
from . import views

# Code has been used from the Code Institute Boutique Ado
# Walkthrough project

urlpatterns = [
    path('', views.index, name='home'),
    path('terms/', views.terms, name='terms'),
]
