from django.contrib.gis.db.models import PolygonField, MultiPolygonField
from django.contrib.postgres.fields import JSONField
from django.db import models


# Create your models here.
class Participant(models.Model):
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=100)
    experienced = models.BooleanField(default=False)
    nationality = models.CharField(max_length=200)
    know_microtasking = models.BooleanField(default=False)

    def __str__(self):
        return '%s %s' % (self.id, self.gender)


class Task(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description_geom = models.TextField()
    description_meta = models.TextField()
    num_of_elements = models.IntegerField(default=0)
    num_of_conflicts = models.IntegerField(default=0)
    has_reward = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('has_reward', 'num_of_elements',)

    def get_all_task_elements(self):
        return self.task_element.all()

    def get_all_task_conflicts(self):
        return self.task_conflict.all()


class TaskElement(models.Model):
    tasks = models.ManyToManyField(Task, related_name='task_element')
    title = models.CharField(max_length=200)
    building_nr = models.IntegerField(null=True, blank=True)
    info1 = models.CharField(max_length=200)
    info2 = models.CharField(max_length=200)
    info3 = models.CharField(max_length=200)
    element_name = models.CharField(max_length=200)
    element_geom = MultiPolygonField(null=True, blank=True)
    json = JSONField(blank=True)
    is_imported = models.BooleanField(default=False)

    def __str__(self):
        return self.element_name


class TaskConflict(models.Model):
    tasks = models.ManyToManyField(Task, related_name='task_conflict')
    element = models.OneToOneField(TaskElement, related_name='conflict', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default='No title')
    building_nr = models.IntegerField(null=True, blank=True)
    info1 = models.CharField(max_length=200)
    info2 = models.CharField(max_length=200)
    info3 = models.CharField(max_length=200)
    conflict_name = models.CharField(max_length=200)
    conflict_geom = MultiPolygonField(null=True, blank=True)
    json = JSONField(blank=True)
    is_fixed = models.BooleanField(default=False)

    def __str__(self):
        return self.conflict_name
