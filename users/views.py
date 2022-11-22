from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from .forms import CustomUserCreationForm, ProfileForm
# Create your views here.

def login_user(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try: 
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Username or password is wrong')

    return render(request, 'users/login_register.html')


def logout_user(request):
    logout(request)
    messages.error(request, 'User logout!')
    return redirect('login')


def register_user(request):
    page = 'register'
    form = CustomUserCreationForm

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User created succesfully')

            login(request, user)
            return redirect('edit-account')
        
        else:
            messages.error(request, 'Something went wrong, try again!')

    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)


def profiles(request):
    profiles = Profile.objects.all()
    contex = {'profiles': profiles}
    return render(request, 'users/profiles.html', contex)


def userprofile(request, pk):
    profile = Profile.objects.get(id=pk)

    topskill = profile.skill_set.exclude(description="")
    otherskills = profile.skill_set.filter(description="")

    context = {'profile': profile, 'topskill': topskill, 'otherskills': otherskills}
    return render(request, 'users/user-profile.html', context)


@login_required(login_url='login')
def user_account(request):
    profile = request.user.profile

    skills = profile.skill_set.all()
    projects = profile.project_set.all()

    context = {'profile': profile, 'skills': skills, 'projects': projects}
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def edit_account(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
    
            return redirect('account')
    context = {'form': form}
    return render(request, 'users/profile_form.html', context)

    