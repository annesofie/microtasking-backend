# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20170208_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskconflict',
            name='tasks',
            field=models.ManyToManyField(related_name='task_conflict', to='base.Task'),
        ),
    ]
