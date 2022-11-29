from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile, Skill, Inbox
from .forms import CustomUserCreationForm, ProfileForm, SkillForm
from django.db.models import Q
from .help_funcs import search_profiles
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.

def login_user(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == "POST":
        username = request.POST['username'].lower()
        password = request.POST['password']

        try: 
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')
        else:
            messages.error(request, 'Username or password is wrong')

    return render(request, 'users/login_register.html')


def logout_user(request):
    logout(request)
    messages.info(request, 'User was logged out!')
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
    profiles, search_query = search_profiles(request)
    page = request.GET.get('page')
    results = 6
    paginator = Paginator(profiles, results)

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)


    contex = {'profiles': profiles, 'search_query': search_query}
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

    
@login_required(login_url='login')
def create_skill(request):
    form = SkillForm
    profile = request.user.profile

    if request.method == "POST":
        form = SkillForm(request.POST) 
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, 'Skill added')
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/skill_form.html', context)


@login_required(login_url='login')
def update_skill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)

    if request.method == "POST":
        form = SkillForm(request.POST, instance=skill) 
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill updated')
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/skill_form.html', context)


@login_required(login_url='login')
def delete_skill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)

    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill was deleted succesfully')
        return redirect('account')

    context = {'object': skill}
    return render(request, 'users/delete_object.html', context)


@login_required(login_url='login')
def inbox(request):
    profile = request.user.profile
    messages_inbox = profile.messages.all()
    unread = messages_inbox.filter(is_read=False).count()

    context = {'messages_inbox': messages_inbox, 'unread': unread}
    return render(request, 'users/inbox.html', context)