# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 16:44
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20170208_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskconflict',
            name='task_conflict',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326),
        ),
    ]
