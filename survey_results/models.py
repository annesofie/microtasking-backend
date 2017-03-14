
from django.db import models


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

