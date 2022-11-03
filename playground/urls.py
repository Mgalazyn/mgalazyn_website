from django.urls import path, include
from . import views


#  URLconf
urlpatterns = [
    path('playground', views.project, name="project"),
    path('hi/', views.first_words)
]
