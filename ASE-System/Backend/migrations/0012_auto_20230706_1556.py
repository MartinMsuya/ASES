# Generated by Django 3.2.19 on 2023-07-06 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0011_alter_numberplate_record_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='plate',
        ),
        migrations.AddField(
            model_name='test',
            name='Message_plate',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
