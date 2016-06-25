# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-25 11:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0003_auto_20160625_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='speech',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 6, 25, 11, 37, 17, 777177, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speech',
            name='updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 6, 25, 11, 37, 19, 212622, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='talk',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 6, 25, 11, 37, 20, 576319, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='talk',
            name='updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 6, 25, 11, 37, 21, 782675, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 6, 25, 11, 37, 23, 418591, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 6, 25, 11, 37, 24, 722598, tzinfo=utc)),
            preserve_default=False,
        ),
    ]