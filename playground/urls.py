from django.urls import path, include
from . import views


#  URLconf
urlpatterns = [
    path('playground/project', views.project, name="project"),
    path('playground', views.first_words)
]
