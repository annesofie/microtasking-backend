from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import Tasksurvey, Taskresult
from .serializers import TasksurveySerializer, TaskresultSerializer


class TasksurveyViewSet(viewsets.ModelViewSet):
    queryset = Tasksurvey.objects.all()
    serializer_class = TasksurveySerializer


class TaskresultViewSet(viewsets.ModelViewSet):
    queryset = Taskresult.objects.all()
    serializer_class = TaskresultSerializer
