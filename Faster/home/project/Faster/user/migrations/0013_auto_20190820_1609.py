# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-08-20 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20190820_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateTimeField(blank=True, default='1979-08-28', null=True, verbose_name='生日'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nick_name',
            field=models.CharField(default='虚拟-Wendy Alvarez', max_length=255, verbose_name='昵称'),
        ),
    ]
