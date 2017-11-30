# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-30 20:34
from __future__ import unicode_literals

from django.db import migrations


def forward(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Message = apps.get_model("mailing", "Message")
    MessageAuthor = apps.get_model("mailing", "MessageAuthor")
    for message in Message.objects.using(db_alias).all():
        message.new_author, _ = MessageAuthor.objects.using(db_alias).get_or_create(author_type=message.author_type, author_id=message.author_id)
        message.save()


def backward(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Message = apps.get_model("mailing", "Message")
    ContentType = apps.get_model("contenttypes", "ContentType")
    for message in Message.objects.using(db_alias).all():
        author_type = message.new_author.author_type
        message.author_type = message.new_author.author_type
        message.author_id = message.new_author.author_id
        AuthorType = apps.get_model(author_type.app_label, author_type.model)
        author = AuthorType.objects.get(pk=message.author_id)
        if author_type.model == 'conference':
            message.from_email = author.contact_email
        else:
            message.from_email = author.email
        message.save()


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0003_auto_20171129_2155'),
    ]

    operations = [
        migrations.RunPython(forward, backward),
    ]
