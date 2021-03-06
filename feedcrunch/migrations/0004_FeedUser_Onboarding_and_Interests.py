# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-10 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedcrunch', '0003_interest'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeduser',
            name='interests',
            field=models.ManyToManyField(related_name='users_by_interest', to='feedcrunch.Interest'),
        ),
        migrations.AddField(
            model_name='feeduser',
            name='onboarding_done',
            field=models.BooleanField(default=False),
        ),
    ]
