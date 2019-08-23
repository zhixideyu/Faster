# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-08-20 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0006_auto_20190819_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='RssResultInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=50, null=True)),
                ('publish_time', models.CharField(blank=True, max_length=50, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'rss_result_info',
                'verbose_name_plural': '根据RSS规则爬取的内容',
                'verbose_name': '根据RSS规则爬取的内容',
            },
        ),
    ]
