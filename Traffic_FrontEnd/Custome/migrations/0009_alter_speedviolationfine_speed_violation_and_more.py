# Generated by Django 4.2.1 on 2023-05-08 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Custome", "0008_alter_speedviolationfine_speed_violation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="speedviolationfine",
            name="speed_violation",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="Custome.speedviolation"
            ),
        ),
        migrations.CreateModel(
            name="FilteredViolation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_On", models.DateTimeField(auto_now_add=True)),
                (
                    "speedfine",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Custome.speedviolationfine",
                    ),
                ),
                (
                    "speedviolation",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Custome.speedviolation",
                    ),
                ),
            ],
        ),
    ]