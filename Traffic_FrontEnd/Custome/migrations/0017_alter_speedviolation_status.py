# Generated by Django 4.2.1 on 2023-05-23 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Custome', '0016_alter_speedviolation_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speedviolation',
            name='status',
            field=models.CharField(choices=[('Unpaid', 'Unpaid'), ('Paid', 'Paid')], default='Unpaid', max_length=10),
        ),
    ]
