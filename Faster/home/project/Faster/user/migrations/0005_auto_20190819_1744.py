# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-08-19 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20190819_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateTimeField(blank=True, default='1923-03-29', null=True, verbose_name='生日'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nick_name',
            field=models.CharField(default='虚拟-Michelle Smith', max_length=255, verbose_name='昵称'),
        ),
    ]
