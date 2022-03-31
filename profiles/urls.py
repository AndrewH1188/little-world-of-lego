from django.urls import path
from . import views

# Code has been used from the Code Institute Boutique Ado
# Walkthrough project

urlpatterns = [
    path('', views.profile, name='profile'),
]
