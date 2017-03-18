from django.contrib import admin

# Register your models here.
from .models import Tasksurvey, Taskresult


@admin.register(Tasksurvey)
class TasksurveyAdmin(admin.ModelAdmin):
    list_filter = ['interupted']
    search_fields = ['difficulty']


@admin.register(Taskresult)
class TaskresultAdmin(admin.ModelAdmin):
    list_filter = ['date']
    search_fields = ['totaltime']
