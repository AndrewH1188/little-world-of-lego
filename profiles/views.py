from django.shortcuts import render, get_object_or_404

from .models import UserProfile

# Code has been used from the Code Institute Boutique Ado
# Walkthrough project

def profile(request):
    """ Display the user's profile. """
    # profile = get_object_or_404(UserProfile, user=request.user) 
    
    # Look into the above, It works ok so far without, 
    # but chucks up a 404 with this uncommented. although 
    # the user name of their profile isn't displayed

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)