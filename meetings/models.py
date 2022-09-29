from pyexpat import model
from django.db import models
from datetime import time

class Meeting(models.Model):
    title = models.CharField(max_length=200, default='meeting')
    date = models.DateField()
    startTime = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.title} on {self.date} at {self.startTime} for {self.duration} hours"