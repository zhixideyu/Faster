# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-08-26 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0016_auto_20190822_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='rssinfospider',
            name='type',
            field=models.CharField(default='html', max_length=20, null=True, verbose_name='数据类型'),
        ),
    ]