from django.urls import path, include
from . import views


#  URLconf
urlpatterns = [
    path('project/<str:pk>', views.project, name='project'),
    path('main', views.project, name='main'),
    path('create-project/', views.create_project, name='create-project'),
    path('update-project/<str:pk>/', views.update_project, name='update-project'),
    path('delete-project/<str:pk>/', views.delete_project, name='delete-project'),
]
