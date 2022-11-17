from django.shortcuts import render
from .models import Profile
# Create your views here.

def profiles(request):
    profiles = Profile.objects.all()
    contex = {'profiles': profiles}
    return render(request, 'users/profiles.html', contex)


def userprofile(request, pk):
    profile = Profile.objects.get(id=pk)

    topskill = profile.skill_set.exclude(description="")
    otherskills = profile.skill_set.filter(description="")

    contex = {'profile': profile, 'topskill': topskill, 'otherskills': otherskills}
    return render(request, 'users/user-profile.html', contex)