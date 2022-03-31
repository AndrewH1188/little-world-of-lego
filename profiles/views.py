from django.shortcuts import render

# Code has been used from the Code Institute Boutique Ado
# Walkthrough project

def profile(request):
    """ Display the users profile """
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
