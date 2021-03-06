# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 01:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('feedcrunch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RSSFeed',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('link', models.URLField(max_length=2000)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('bad_attempts', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='RSSFeed_Sub',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_sub_feed_assoc', to='feedcrunch.RSSFeed')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_sub_feed', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RSSArticle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('link', models.URLField(max_length=2000)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('guid', models.UUIDField(blank=True, default=uuid.uuid4, null=True)),
                ('creator', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('content', models.TextField(blank=True, default='', null=True)),
                ('media', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('pub_date', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('rssfeed', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rel_rss_feed_articles', to='feedcrunch.RSSFeed')),
            ],
        ),
        migrations.CreateModel(
            name='RSSArticle_Assoc',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('open_count', models.SmallIntegerField(default=0)),
                ('marked_read', models.BooleanField(default=False)),
                ('reposted', models.BooleanField(default=False)),
                ('recommendation_score', models.FloatField(default=0)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_sub_article_assoc', to='feedcrunch.RSSArticle')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_sub_article', to=settings.AUTH_USER_MODEL)),
                ('subscribtion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rel_sub_feedsub_article', to='feedcrunch.RSSFeed_Sub')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='rssfeed_sub',
            unique_together=set([('user', 'feed')]),
        ),
        migrations.AlterUniqueTogether(
            name='rssarticle_assoc',
            unique_together=set([('user', 'article')]),
        ),
    ]
