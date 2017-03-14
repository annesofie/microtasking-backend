from rest_framework import serializers

from .models import Tasksurvey


class TasksurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasksurvey
        fields = '__all__'