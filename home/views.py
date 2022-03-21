from django.shortcuts import render

# Code has been used from the Code Institute Boutique Ado
# Walkthrough project

def index(request):
    """ A view to return the index page """
    
    return render(request, 'home/index.html')
