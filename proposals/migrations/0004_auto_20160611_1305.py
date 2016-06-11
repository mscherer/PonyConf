# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 13:05
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0003_auto_20160608_2002'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='speach',
            options={'ordering': ['talk', 'order']},
        ),
        migrations.AlterField(
            model_name='speach',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.PonyConfSpeaker'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='speakers',
            field=models.ManyToManyField(through='proposals.Speach', to='accounts.PonyConfSpeaker'),
        ),
    ]
