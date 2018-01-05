# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-04 01:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20180103_2026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='palette',
            name='id',
        ),
        migrations.RemoveField(
            model_name='series',
            name='id',
        ),
        migrations.AlterField(
            model_name='palette',
            name='archetype_name',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='series_name',
            field=models.CharField(max_length=250, primary_key=True, serialize=False, unique=True),
        ),
    ]
