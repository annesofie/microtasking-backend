# used for our data representations

from django.contrib.auth.models import User, Group
from .models import Profile, Task, TaskElement, TaskConflict, Participant
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer


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


class TaskElementSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = TaskElement
        geo_field = "element_geom"
        exclude = ('tasks',)


class TaskConflictSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = TaskConflict
        geo_field = "conflict_geom"
        exclude = ('tasks',)


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'