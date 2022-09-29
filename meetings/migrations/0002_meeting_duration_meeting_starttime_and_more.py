# Generated by Django 4.1.1 on 2022-09-27 11:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='duration',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='meeting',
            name='startTime',
            field=models.TimeField(default=datetime.time(9, 0)),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='title',
            field=models.CharField(default='meeting', max_length=200),
        ),
    ]