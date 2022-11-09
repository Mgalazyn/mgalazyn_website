from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
# Create your views here.
# request handler

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    contex = {'project': projectObj}
    return render(request, 'single_project.html', contex)


def projects(request):
    projects = Project.objects.all()
    contex = {'projects': projects}
    return render(request, 'projects.html', contex)


def create_project(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main')
    contex = {'form': form}
    return render(request, 'project_form.html', contex)


def update_project(request, pk):
    projectt = Project.objects.get(id=pk)
    form = ProjectForm(instance=projectt)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('main')
    contex = {'form': form}
    return render(request, 'project_form.html', contex)


def delete_project(request, pk):
    project = Project.objects.get(id=pk)

    if request.method =='POST':
        project.delete()
        return redirect('main')

    contex = {'object': project}
    return render(request, 'delete_object.html', contex)
