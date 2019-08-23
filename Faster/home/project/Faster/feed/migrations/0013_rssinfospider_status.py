# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-08-20 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0012_auto_20190820_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='rssinfospider',
            name='status',
            field=models.CharField(choices=[('d', '禁用'), ('p', '正常')], default='p', max_length=1, verbose_name='规则状态'),
        ),
    ]
