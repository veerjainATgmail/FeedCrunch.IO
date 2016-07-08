# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 12:10
from __future__ import unicode_literals

from django.db import migrations, models
import encrypted_fields.fields


class Migration(migrations.Migration):

	dependencies = [
		('feedcrunch', '0002_feeduser_profile_picture'),
	]

	operations = [
		migrations.CreateModel(
			name='Options',
			fields=[
				('parameter', models.CharField(max_length=255, primary_key=True, serialize=False)),
				('value', encrypted_fields.fields.EncryptedCharField(default='', max_length=255)),
			],
		),
	]
