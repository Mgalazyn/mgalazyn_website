from django.shortcuts import render
from .models import Project
# Create your views here.
# request handler


def first_words(request):
    context = {'name': 'Marcin\'s web'}
    return render(request, 'hello.html', context)


def project(request):
    # PyCHARM PROBLEM to show objects from class need to resolve
    projects = Project.objects.all()
    tags = projects.tags.all()
    contex = {'projects': projects, 'tags': tags}
    return render(request, 'single_project.html', contex)

