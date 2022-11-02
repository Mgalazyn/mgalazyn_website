from django.urls import path
from . import views


#  URLconf
urlpatterns = [
    path('hi/', views.first_words)
]
