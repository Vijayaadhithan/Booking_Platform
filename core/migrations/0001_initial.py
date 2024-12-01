# Generated by Django 5.0.7 on 2024-12-01 12:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Membership",
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
                ("name", models.CharField(max_length=100)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("duration", models.PositiveIntegerField()),
                ("benefits", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Service",
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
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("base_price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("unit_price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="ServiceProvider",
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
                ("name", models.CharField(max_length=255)),
                ("service_type", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=255)),
                ("availability", models.JSONField()),
                ("rating", models.FloatField(default=0)),
                (
                    "profile_picture",
                    models.ImageField(
                        blank=True, null=True, upload_to="provider_pictures/"
                    ),
                ),
                ("certifications", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="User",
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
                ("username", models.CharField(max_length=255, unique=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("phone_number", models.CharField(max_length=15, unique=True)),
                ("password", models.CharField(max_length=255)),
                (
                    "profile_picture",
                    models.ImageField(
                        blank=True, null=True, upload_to="profile_pictures/"
                    ),
                ),
                ("date_joined", models.DateTimeField(auto_now_add=True)),
                (
                    "membership_status",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core.membership",
                    ),
                ),
            ],
        ),
    ]
