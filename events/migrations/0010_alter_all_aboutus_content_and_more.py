# Generated by Django 4.1.1 on 2022-09-26 08:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0009_rename_all_abouts_all_aboutus"),
    ]

    operations = [
        migrations.AlterField(
            model_name="all_aboutus",
            name="content",
            field=models.TextField(max_length=10000, verbose_name="Experience"),
        ),
        migrations.AlterField(
            model_name="information",
            name="refresh_date",
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name="paper",
            name="papercontent",
            field=models.TextField(max_length=10000, verbose_name="Papercontent"),
        ),
    ]