# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-24 19:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0004_auto_20190124_1733'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='todo',
            new_name='list',
        ),
    ]