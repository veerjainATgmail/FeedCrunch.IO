# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-07 23:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedcrunch', '0018_feeduser_modified_facebook_credentials'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feeduser',
            old_name='linkedin_token',
            new_name='linkedin_access_token',
        ),
        migrations.RemoveField(
            model_name='feeduser',
            name='linkedin_token_secret',
        ),
        migrations.AddField(
            model_name='feeduser',
            name='linkedin_token_expire_datetime',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
