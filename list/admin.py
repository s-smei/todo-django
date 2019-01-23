# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Todo, Element


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'name')


@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    list_display = ('id', 'todo', 'name', 'is_finished')
