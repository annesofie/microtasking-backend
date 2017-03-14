from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import Tasksurvey
from .serializers import TasksurveySerializer


class TasksurveyViewSet(viewsets.ModelViewSet):
    queryset = Tasksurvey.objects.all()
    serializer_class = TasksurveySerializer