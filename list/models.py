# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.


class List(models.Model):
    owner = models.ForeignKey(User,
                              related_name="list_owner")

    name = models.CharField(
        max_length=100,
        blank=False,
    )

    start_time = models.DateTimeField(auto_now_add=True)
    is_finished = models.BooleanField(default=True)

    def get_is_finished(self):
        """Return True only if there is no unfinished item"""
        for item in self.item_set.all():
            if not item.is_finished:
                return False
        return True

    def get_absolute_url(self):
        return reverse('list_todo_show', args=[self.id])

    def new_item(self):
        return Item(
            list=self,
            is_finished=False
        )

    def __str__(self):
        return "{0} list by {1}".format(
            self.name, self.owner
        )


class Item(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False
    )
    is_finished = models.BooleanField(editable=True, default=False)

    list = models.ForeignKey(List)

    def __str__(self):
        status = 'finished' if self.is_finished else 'in progress'
        return "{0}   {1}".format(self.name, status)
