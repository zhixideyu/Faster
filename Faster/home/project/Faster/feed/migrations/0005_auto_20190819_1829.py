# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-08-19 18:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_rssinfospider_encode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rssinfospider',
            old_name='connect',
            new_name='connect_rule',
        ),
        migrations.RenameField(
            model_name='rssinfospider',
            old_name='feed_title',
            new_name='feed_title_rule',
        ),
    ]
