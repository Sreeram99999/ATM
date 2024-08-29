# Generated by Django 5.0.6 on 2024-08-28 06:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Acc_type",
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
                ("acc_type", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Gender",
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
                ("gender", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="History",
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
                ("acc_num", models.BigIntegerField()),
                ("type", models.CharField(max_length=50)),
                ("amt", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="Register",
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
                ("acc_num", models.BigIntegerField(editable=False, unique=True)),
                ("eny_pin", models.CharField(max_length=100)),
                (
                    "balance",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                ("first_name", models.CharField(max_length=50)),
                ("middle_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("address", models.TextField()),
                ("mail", models.EmailField(max_length=254, unique=True)),
                (
                    "acc_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.acc_type"
                    ),
                ),
                (
                    "gender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.gender"
                    ),
                ),
            ],
        ),
    ]
