from django.shortcuts import render
from .models import Profile
# Create your views here.

def profiles(request):
    profiles = Profile.objects.all()
    contex = {'profiles': profiles}
    return render(request, 'users/profiles.html', contex)


def userprofile(request, pk):
    profile = Profile.objects.get(id=pk)
    contex = {'profile': profile}
    return render(request, 'users/user-profile.html', contex)