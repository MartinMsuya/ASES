# Generated by Django 4.2.1 on 2023-05-07 18:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("Custome", "0006_rename_dept_status_speedviolationfine_paid"),
    ]

    operations = [
        migrations.AddField(
            model_name="speedviolation",
            name="record_date",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
