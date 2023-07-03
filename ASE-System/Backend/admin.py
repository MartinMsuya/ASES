from django.contrib import admin
from .models import Numberplate, Test
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.

class NumberplateImportExport(ImportExportActionModelAdmin, admin.ModelAdmin):
    ...
admin.site.register(Numberplate, NumberplateImportExport)

class NumberplateAdmin(admin.ModelAdmin):
    list_display = ('No_plate', 'Image', 'Car_speed', 'Location', 'Fine_amount', 'Status', 'Record_date')


admin.site.register(Test)