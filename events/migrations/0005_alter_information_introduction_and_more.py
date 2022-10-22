# Generated by Django 4.1.1 on 2022-09-21 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0004_rename_event_date_information_refresh_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="information",
            name="introduction",
            field=models.CharField(max_length=50, verbose_name="Introduction"),
        ),
        migrations.AlterField(
            model_name="information",
            name="recent_events",
            field=models.CharField(max_length=50, verbose_name="Recent_events"),
        ),
        migrations.AlterField(
            model_name="information",
            name="refresh_date",
            field=models.CharField(max_length=50, verbose_name="refresh_date"),
        ),
    ]
