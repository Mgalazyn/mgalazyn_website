from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request handler


def first_words(request):
    return render(request, 'hello.html', {'name': 'Marcin\'s web'})

