from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request handler


def first_words(request):
    page = 'project'
    number = 9
    context = {'name': 'Marcin\'s web', 'page': page, 'number': number}
    return render(request, 'hello.html', context)


def project(request):
    return render(request, 'single_project.html')

