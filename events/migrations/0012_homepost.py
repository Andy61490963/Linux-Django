# Generated by Django 4.1.2 on 2022-10-21 04:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0011_portfolio_alter_all_aboutus_content"),
    ]

    operations = [
        migrations.CreateModel(
            name="homepost",
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
                ("postname", models.CharField(max_length=20, verbose_name="Name")),
                (
                    "introduction",
                    models.TextField(max_length=500, verbose_name="Introduction"),
                ),
                (
                    "post_date",
                    models.DateTimeField(blank=True, default=datetime.datetime.now),
                ),
            ],
        ),
    ]
