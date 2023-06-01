from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _




# Create your models here.
class SpeedViolation(models.Model):

    STATUS_CHOICES = [
        ('Unpaid', 'Unpaid'),
        ('Paid', 'Paid'),
    ]

    number_plate = models.CharField(max_length=20)
    car_image = models.ImageField(upload_to='speed_violations/')
    speed_limit = models.IntegerField()
    car_speed = models.IntegerField()
    exceed_speed = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=20, null=True, blank=True)
    fine_amount = models.DecimalField(_('Fine Amount'), max_digits=8, decimal_places=2, default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Unpaid')
    record_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.exceed_speed = self.car_speed - self.speed_limit
        super().save(*args, **kwargs)
        return str(self.number_plate)
    

@receiver(pre_save, sender=SpeedViolation)
def calculate_fine_amount(sender, instance, **kwargs):
    if instance.exceed_speed >= 5:
        instance.fine_amount = 30000
    else:
        instance.fine_amount = 0
    