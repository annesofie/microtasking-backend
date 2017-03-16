
from django.db import models
from django.contrib.postgres.fields import JSONField


# Create your models here.
class Tasksurvey(models.Model):
    difficulty = models.CharField(max_length=20, blank=True)
    besteffort = models.NullBooleanField(default=None)
    interupted = models.NullBooleanField(default=None)
    comment = models.CharField(max_length=200, blank=True)
    participant = models.ForeignKey('base.Participant')
    task = models.ForeignKey('base.Task')

    def __str__(self):
        return self.difficulty


class Taskresult(models.Model):
    geomtasktime = models.IntegerField(blank=True)
    metatasktime = models.IntegerField(blank=True)
    totaltime = models.IntegerField(blank=True)
    numberofcorrectgeomelem = models.IntegerField(blank=True)
    numberofcorrectmetadataelem = models.IntegerField(blank=True)
    selectedgeomlayers = JSONField(blank=True)  ### TODO: Should be an list or array?
    participant = models.ForeignKey('base.Participant')
    task = models.ForeignKey('base.Task')
