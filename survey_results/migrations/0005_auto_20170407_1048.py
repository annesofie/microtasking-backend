# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-07 08:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey_results', '0004_auto_20170407_1012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskresult',
            old_name='correctbuildingnrGeom',
            new_name='correct_buildings_geom',
        ),
        migrations.RenameField(
            model_name='taskresult',
            old_name='correctbuildingnrMeta',
            new_name='correct_buildings_meta',
        ),
    ]