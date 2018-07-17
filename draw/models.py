from django.db import models
from django.utils import timezone

# Create your models here.
class Event(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=30)
    time = models.CharField(max_length=10)
    current = models.IntegerField(default=1)
    maximum = models.IntegerField(default=5)
    
    
    