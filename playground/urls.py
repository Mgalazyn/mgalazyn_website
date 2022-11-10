from django.urls import path, include
from . import views


#  URLconf
urlpatterns = [
    path('main', views.projects, name='main'),
    path('view-project/<str:pk>/', views.project, name='view-project'),
    path('create-project/', views.create_project, name='create-project'),
    path('update-project/<str:pk>/', views.update_project, name='update-project'),
    path('delete-project/<str:pk>/', views.delete_project, name='delete-project'),
]
