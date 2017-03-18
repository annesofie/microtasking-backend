from rest_framework import serializers

from .models import Tasksurvey, Taskresult


class TasksurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasksurvey
        fields = '__all__'


class TaskresultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taskresult
        fields = '__all__'
