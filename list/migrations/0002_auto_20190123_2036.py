# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-23 20:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_finished', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameModel(
            old_name='List',
            new_name='Todo',
        ),
        migrations.RemoveField(
            model_name='item',
            name='list',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.AddField(
            model_name='element',
            name='todo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='list.Todo'),
        ),
    ]
