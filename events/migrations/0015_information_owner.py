# Generated by Django 4.1.1 on 2022-10-24 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_alter_homepost_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='owner',
            field=models.IntegerField(default=1, verbose_name='Information Owner'),
        ),
    ]
