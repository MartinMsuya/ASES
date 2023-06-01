import uuid
from django.db import models
from django.contrib.auth.models import User




# Create your models here.
 
class Projects(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank=True)
    title = models.CharField(max_length=30, default=None)
    descripttion = models.TextField()
    number = models.FloatField(default=None) 
        
    def __str__(self):
        return str(self.title)