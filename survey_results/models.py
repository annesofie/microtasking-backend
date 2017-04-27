from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
from django.utils.datetime_safe import datetime


class Tasksurvey(models.Model):
    difficulty = models.CharField(max_length=20)
    besteffort = models.NullBooleanField(default=False)
    interupted = models.NullBooleanField(default=False)
    comment = models.CharField(max_length=200, blank=True)
    participant = models.ForeignKey('base.Participant')
    task = models.ForeignKey('base.Task')

    def __str__(self):
        return 'Task: %s, participant: %s' % (self.task, self.participant)

    @property
    def participant_experienced(self):
        return self.participant.experienced



class Taskresult(models.Model):
    date = models.DateTimeField(default=datetime.now)
    taskorder = ArrayField(models.IntegerField())
    geomtasktime = models.IntegerField()
    metatasktime = models.IntegerField()
    totaltime = models.IntegerField(blank=True)
    correctgeom = models.IntegerField(blank=True)
    correctmetadata = models.IntegerField(blank=True)
    correct_buildings_geom = ArrayField(models.IntegerField(blank=True), blank=True, null=True)
    correct_buildings_meta = ArrayField(models.IntegerField(blank=True), blank=True, null=True)
    selectedgeomlayers = JSONField(blank=True)
    selectedmetalayers = JSONField(blank=True)
    participant = models.ForeignKey('base.Participant')
    task = models.ForeignKey('base.Task')

    def __str__(self):
        return 'Task: %s, date: %s' % (self.task, self.date)

    @property
    def participant_age(self):
        return self.participant.age

