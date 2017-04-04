from rest_framework import routers
from django.conf.urls import url

from base import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'task', views.TaskElementConflictViewSet)
router.register(r'participant', views.ParticipantViewSet)


urlpatterns = [

]