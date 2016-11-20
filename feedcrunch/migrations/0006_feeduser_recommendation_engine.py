# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 01:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feedcrunch', '0005_estimator'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeduser',
            name='recommendation_engine',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='feedcrunch.Estimator'),
        ),
    ]