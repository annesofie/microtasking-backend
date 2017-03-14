from django.contrib import admin

# Register your models here.
from .models import Tasksurvey


@admin.register(Tasksurvey)
class TasksurveyAdmin(admin.ModelAdmin):
    list_filter = ['interupted']
    search_fields = ['difficulty']
