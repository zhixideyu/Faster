# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-08-19 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_rssinfospider_xml_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='rssinfospider',
            name='encode',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='编码格式'),
        ),
    ]