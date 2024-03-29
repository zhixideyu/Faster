# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-08-14 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RssSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('href', models.CharField(max_length=225, verbose_name='RSS地址')),
                ('title', models.CharField(max_length=50, verbose_name='RSS描述')),
                ('status', models.CharField(choices=[('d', '测试'), ('p', '发布'), ('s', '私有')], default='p', max_length=1, verbose_name='RSS状态')),
            ],
            options={
                'verbose_name': 'RSS订阅',
                'verbose_name_plural': 'RSS订阅',
                'db_table': 'rss_subscription',
            },
        ),
    ]
