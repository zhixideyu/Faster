# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-08-19 18:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_auto_20190819_1829'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rssinfospider',
            old_name='feed_url',
            new_name='url',
        ),
    ]
