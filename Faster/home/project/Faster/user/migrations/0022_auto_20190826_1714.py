# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-08-26 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0021_auto_20190822_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateTimeField(blank=True, default='1921-06-12', null=True, verbose_name='生日'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nick_name',
            field=models.CharField(default='虚拟-Miss Sierra Bates MD', max_length=255, verbose_name='昵称'),
        ),
    ]
