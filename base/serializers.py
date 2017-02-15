# used for our data representations

from django.contrib.auth.models import User, Group
from .models import Profile, Task, TaskElement, TaskConflict
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'gender', 'country', 'age')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskElement
        fields = '__all__'


class TaskConflictSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskConflict
        fields = '__all__'
