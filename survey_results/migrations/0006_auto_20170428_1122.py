# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-28 09:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey_results', '0005_auto_20170407_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskresult',
            name='tasknumber',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taskresult',
            name='taskordernumber',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taskresult',
            name='total_correct_elements',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tasksurvey',
            name='taskresult',
            field=models.ForeignKey(default=73, on_delete=django.db.models.deletion.CASCADE, to='survey_results.Taskresult'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='taskresult',
            name='correctgeom',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='taskresult',
            name='correctmetadata',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='taskresult',
            name='totaltime',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tasksurvey',
            name='difficulty',
            field=models.IntegerField(),
        ),
    ]