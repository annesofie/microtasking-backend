from django.contrib.auth.models import User
from django.contrib.gis.db.models import PolygonField, MultiPolygonField
from django.contrib.postgres.fields import JSONField
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Task(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    num_of_elements = models.IntegerField(default=0)
    num_of_conflicts = models.IntegerField(default=0)
    has_reward = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('has_reward', 'num_of_elements',)

    def get_all_task_elements(self):
        # return TaskObject.objects.filter(task=self)
        return self.task_element.all()

    def get_all_task_conflicts(self):
        # return TaskObject.objects.filter(task=self)
        return self.task_conflict.all()


class TaskElement(models.Model):
    tasks = models.ManyToManyField(Task, related_name='task_element')
    title = models.CharField(max_length=200)
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
    title = models.CharField(max_length=200, default='No title')
    info1 = models.CharField(max_length=200)
    info2 = models.CharField(max_length=200)
    info3 = models.CharField(max_length=200)
    conflict_name = models.CharField(max_length=200)
    conflict_geom = MultiPolygonField(null=True, blank=True)
    json = JSONField(blank=True)
    is_fixed = models.BooleanField(default=False)

    def __str__(self):
        return self.conflict_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    age = models.IntegerField(null=True, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
