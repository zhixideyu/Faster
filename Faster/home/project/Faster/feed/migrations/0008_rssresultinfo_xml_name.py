# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-08-20 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0007_rssresultinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='rssresultinfo',
            name='xml_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]