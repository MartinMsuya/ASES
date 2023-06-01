from django.contrib import admin
from .models import SpeedViolation


# Register your models here.
@admin.register(SpeedViolation)

class SpeedViolationAdmin(admin.ModelAdmin):
    list_display = ('number_plate', 'speed_limit', 'car_speed', 'exceed_speed')
    search_fields = ('number_plate',)