# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-08-19 18:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20190819_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateTimeField(blank=True, default='1947-08-30', null=True, verbose_name='生日'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nick_name',
            field=models.CharField(default='虚拟-Cassandra Schneider', max_length=255, verbose_name='昵称'),
        ),
    ]