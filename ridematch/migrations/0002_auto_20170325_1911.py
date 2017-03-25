# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-25 23:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ridematch', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driverevent',
            name='day',
        ),
        migrations.RemoveField(
            model_name='driverevent',
            name='time',
        ),
        migrations.RemoveField(
            model_name='passengerevent',
            name='day',
        ),
        migrations.RemoveField(
            model_name='passengerevent',
            name='email',
        ),
        migrations.AddField(
            model_name='driverevent',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 25, 23, 11, 25, 422043, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='passengerevent',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 25, 23, 11, 31, 491387, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
