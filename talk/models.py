from django.db import models
from django.utils import timezone

class Talk(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    speaker = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    talk_start = models.DateTimeField(blank=True, null=True, default=None)
    talk_end = models.DateTimeField(blank=True, null=True, default=None)
