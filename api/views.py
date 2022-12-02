from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProjectSerializer
from playground.models import Project


@api_view(['GET'])
def get_ways(request):
    ways = [
        {'GET': 'api/projects'},
        {'GET': 'api/projects/id'},
        {'POST': 'api/projects/id/vote'},

        {'POST': 'api/users/token'},
        {'POST': 'api/users/token/refresh'},
    ]

    return Response(ways)


@api_view(['GET'])
def get_projects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True).data

    return Response(serializer)


@api_view(['GET'])
def get_project(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project, many=False).data

    return Response(serializer)