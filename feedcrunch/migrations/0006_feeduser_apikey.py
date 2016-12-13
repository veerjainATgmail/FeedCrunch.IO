# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-13 20:39
from __future__ import unicode_literals

from django.db import migrations, models
import uuid

def gen_uuid(apps, schema_editor):
    MyModel = apps.get_model('feedcrunch', 'feeduser')
    for row in FeedUser.objects.all():
        row.apikey = uuid.uuid4()
        row.save()

class Migration(migrations.Migration):

    dependencies = [
        ('feedcrunch', '0005_remove_feeduser_apikey'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeduser',
            name='apikey',
            field=models.UUIDField(default=uuid.uuid4, editable=False, null=True),
        ),
    ]
