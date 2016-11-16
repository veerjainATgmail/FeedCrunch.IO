# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 23:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedcrunch', '0007_auto_20161115_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='rssarticle',
            name='marked_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='rssarticle',
            name='open_count',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rssarticle',
            name='reposted',
            field=models.BooleanField(default=False),
        ),
    ]
