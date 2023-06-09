# Generated by Django 4.2.1 on 2023-07-01 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Numberplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Record_date', models.DateTimeField(auto_created=True, default=None)),
                ('No_plate', models.CharField(max_length=12)),
                ('Image', models.CharField(max_length=100)),
                ('Car_speed', models.CharField(default='', max_length=5)),
                ('Location', models.CharField(default=None, max_length=50)),
                ('Fine_amount', models.DecimalField(decimal_places=2, default=30000, max_digits=8)),
                ('Status', models.CharField(choices=[('Unpaid', 'Unpaid'), ('Paid', 'Paid')], default='Unpaid', max_length=10)),
            ],
        ),
    ]
