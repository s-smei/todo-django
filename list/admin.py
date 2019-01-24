# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import List, Item


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'name')


@admin.register(Item)
class ElementAdmin(admin.ModelAdmin):
    list_display = ('id', 'list', 'name', 'is_finished')
