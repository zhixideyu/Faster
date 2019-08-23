# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-08-20 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0008_rssresultinfo_xml_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='rssresultinfo',
            name='feed_titile',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='rssresultinfo',
            name='feed_url',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rssresultinfo',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rssresultinfo',
            name='url',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
