# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 23:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='current_occupancy',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='scan',
            name='datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 10, 6, 23, 15, 3, 39513, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='scan',
            name='scanner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scan', to='api.Scanner'),
        ),
        migrations.AlterField(
            model_name='scanner',
            name='description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='scanner',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scanner', to='api.Location'),
        ),
    ]
