# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField(null=True, blank=True)),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Scan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField(default=datetime.datetime(2016, 8, 11, 3, 11, 22, 573892, tzinfo=utc), null=True, blank=True)),
            ],
            options={
                'ordering': ('datetime',),
            },
        ),
        migrations.CreateModel(
            name='Scanner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=300)),
                ('location', models.ForeignKey(blank=True, to='api.Location', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='scan',
            name='scanner',
            field=models.ForeignKey(blank=True, to='api.Scanner', null=True),
        ),
    ]
