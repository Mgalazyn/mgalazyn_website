from django.shortcuts import render, redirect
from .models import Project, Tag
from .forms import ProjectForm, ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .help_funcs import search_project
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
# request handler

def project(request, pk):
    project = Project.objects.get(id=pk)
    form = ReviewForm

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = project
        review.owner = request.user.profile
        review.save()

        messages.success(request, 'Review added!')
        
    contex = {'project': project, 'form': form}
    return render(request, 'single_project.html', contex)


def projects(request):
    projects, search_query = search_project(request)
    page = request.GET.get('page')
    results = 6
    paginator = Paginator(projects, results)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)

    contex = {'projects': projects, 'search_query': search_query, 'paginator': paginator}
    return render(request, 'projects.html', contex)


@login_required(login_url="login")
def create_project(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('main')
    contex = {'form': form}
    return render(request, 'project_form.html', contex)


@login_required(login_url="login")
def update_project(request, pk):
    profile = request.user.profile
    projectt = profile.project_set.get(id=pk)
    form = ProjectForm(instance=projectt)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('main')
    contex = {'form': form}
    return render(request, 'project_form.html', contex)


@login_required(login_url="login")
def delete_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    if request.method =='POST':
        project.delete()
        return redirect('main')

    contex = {'object': project}
    return render(request, 'delete_object.html', contex)
