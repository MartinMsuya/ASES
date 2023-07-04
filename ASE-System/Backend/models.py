import uuid
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
# Create your models here.
 
class Numberplate(models.Model):
    STATUS_CHOICE = [
        ('Unpaid', 'Unpaid'),
        ('Paid', 'Paid'),
    ]
    No_plate = models.CharField(max_length=12)
    Image = models.CharField(max_length=100)
    Car_speed = models.CharField(max_length=5, default='60')
    Location = models.CharField(max_length=50, default= None)
    Fine_amount = models.FloatField(default=30000)
    Status = models.CharField(max_length=10, choices=STATUS_CHOICE, default= 'Unpaid')
    Record_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.No_plate)
    
@receiver(pre_save, sender=Numberplate)
def calculate_fine_amount(sender, instance, **kwargs):
    if instance:
        instance.Fine_amount = 30000.00


class Test(models.Model):
    Image = models.CharField(max_length=23, null=True)
    plate = models.CharField(max_length=23, null=True)


    def __str__(self):
        return str(self.Image)