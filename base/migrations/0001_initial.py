# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 13:28
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('num_of_obj', models.IntegerField(default=0)),
                ('num_of_conflicts', models.IntegerField(default=0)),
                ('has_reward', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('has_reward', 'num_of_obj'),
            },
        ),
        migrations.CreateModel(
            name='TaskConflict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conflict_name', models.CharField(max_length=200)),
                ('task_conflict', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('json', django.contrib.postgres.fields.jsonb.JSONField(blank=True)),
                ('is_fixed', models.BooleanField(default=False)),
                ('task', models.ManyToManyField(to='base.Task')),
            ],
        ),
        migrations.CreateModel(
            name='TaskObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_name', models.CharField(max_length=200)),
                ('task_object', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
                ('json', django.contrib.postgres.fields.jsonb.JSONField(blank=True)),
                ('is_imported', models.BooleanField(default=False)),
                ('task', models.ManyToManyField(to='base.Task')),
            ],
        ),
    ]
