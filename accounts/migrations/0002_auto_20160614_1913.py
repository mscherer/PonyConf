# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 19:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proposals', '0001_initial'),
        ('accounts', '0001_initial'),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.AddField(
            model_name='participation',
            name='review_topics',
            field=models.ManyToManyField(blank=True, to='proposals.Topic'),
        ),
        migrations.AddField(
            model_name='participation',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site'),
        ),
        migrations.AddField(
            model_name='participation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='participation',
            unique_together=set([('site', 'user')]),
        ),
    ]
