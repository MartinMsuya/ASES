# Generated by Django 4.2.1 on 2023-07-01 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0002_alter_numberplate_record_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numberplate',
            name='Fine_amount',
            field=models.FloatField(default=30000),
        ),
    ]
