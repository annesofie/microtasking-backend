from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, request
from django.contrib.auth.models import User, Group
from rest_framework.decorators import detail_route
from rest_framework.generics import RetrieveAPIView, GenericAPIView
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .models import Profile, Task, TaskElement
from rest_framework import viewsets
from rest_framework.views import APIView
from base.serializers import UserSerializer, GroupSerializer, ProfileSerializer, TaskSerializer, TaskElementSerializer, \
    TaskConflictSerializer


class JSONResponse(HttpResponse):
    """
       An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().select_related('profile').order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @detail_route(methods=['get'], url_path='elements')
    def get_task_elements(self, request, pk):
        task = self.get_object()
        task_elements = task.get_all_task_elements()
        serializer = TaskElementSerializer(task_elements, many=True)
        return Response(serializer.data)

    @detail_route(methods=['get'], url_path='conflicts')
    def get_task_conflicts(self, request, pk):
        task = self.get_object()
        task_conflicts = task.get_all_task_conflicts()
        serializer = TaskConflictSerializer(task_conflicts, many=True)
        return Response(serializer.data)


class TaskElementConflictViewSet(viewsets.ModelViewSet):
    queryset = TaskElement.objects.all()
    serializer_class = TaskElementSerializer

    @detail_route(methods=['get'], url_path='conflict')
    def get_conflict_in_task(self, request, pk):
        task = self.get_object()
        conflict = task.conflict
        serializer = TaskConflictSerializer(conflict)
        return Response(serializer.data)


def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.country = 'Norway'
    user.save()
