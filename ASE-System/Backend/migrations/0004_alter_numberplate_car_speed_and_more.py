# Generated by Django 4.2.1 on 2023-07-01 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0003_alter_numberplate_fine_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numberplate',
            name='Car_speed',
            field=models.CharField(default='60', max_length=5),
        ),
        migrations.AlterField(
            model_name='numberplate',
            name='Location',
            field=models.CharField(default='Mwenge', max_length=50),
        ),
    ]
