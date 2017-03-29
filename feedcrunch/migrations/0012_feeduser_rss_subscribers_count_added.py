# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 07:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedcrunch', '0011_rsssubscriber'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeduser',
            name='rss_subscribers_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rsssubscriber',
            name='ipaddress',
            field=models.GenericIPAddressField(),
        ),
    ]
