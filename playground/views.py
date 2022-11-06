from django.shortcuts import render
from .models import Project
# Create your views here.
# request handler


def first_words(request):
    context = {'name': 'Marcin\'s web'}
    return render(request, 'hello.html', context)


def project(request):
    projects = Project.objects.all()
    contex = {'projects': projects}
    return render(request, 'single_project.html', contex)

