# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Todo(models.Model):
    owner = models.ForeignKey(User,
                              related_name="list_owner")

    name = models.CharField(
        max_length=100,
        blank=False,
    )
    is_finished = models.BooleanField(editable=False, default=False)

    start_time = models.DateTimeField(auto_now_add=True)

    def get_is_finished(self):
        """Return True only if there is no unfinished item"""
        for element in self.element_set.all():
            if not element.is_finished:
                return False
        return True

    def __str__(self):
        return "{0} list by {1}".format(
            self.name, self.owner
        )


class Element(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False
    )
    is_finished = models.BooleanField(editable=True, default=False)

    todo = models.ForeignKey(Todo)
