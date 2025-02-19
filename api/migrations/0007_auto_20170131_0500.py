# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-31 05:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20170119_0034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='current_occupancy',
        ),
        migrations.AddField(
            model_name='location',
            name='_current_occupancy',
            field=models.IntegerField(db_column=b'current_occupancy', default=0),
        ),
        migrations.AlterField(
            model_name='scan',
            name='scanner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scan', to='api.Scanner'),
        ),
        migrations.AlterField(
            model_name='scanner',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scanner', to='api.Location'),
        ),
    ]
