from rest_framework import routers
from django.conf.urls import url

from base import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'profile', views.ProfileViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'task', views.TaskElementConflictViewSet)


urlpatterns = [
]