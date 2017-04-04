# Create your views here.
from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponse, request
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.decorators import detail_route, list_route
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task, TaskElement, Participant, TaskConflict
from rest_framework import viewsets
from base.serializers import ParticipantSerializer, UserSerializer, TaskSerializer, TaskElementSerializer, \
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


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @list_route(url_path='order')
    def get_task_order(self, request):
        set_list = settings.TASK_SET_ORDER
        last_index = cache.get('last_index')
        if not last_index:
            cache.set('last_index', 0, None)
            last_index = 0

        current_task_set = set_list[last_index]
        last_index = last_index + 1 if last_index < len(set_list)-1 else 0
        cache.set('last_index', last_index, None)

        return Response(current_task_set)

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


class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


class BuildingElementsView(APIView):
    def get(self, request, building_nr):
        first = TaskElement.objects.get(building_nr=self.kwargs["building_nr"])
        first_serializer = TaskElementSerializer(first)
        second = TaskConflict.objects.get(building_nr=self.kwargs["building_nr"])
        second_serializer = TaskConflictSerializer(second)
        toreturn = [first_serializer.data, second_serializer.data]
        return Response(toreturn)
