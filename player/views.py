# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from list.models import Todo
# Create your views here.


@login_required()
def home(request):
    my_todos = Todo.objects.filter(owner=request.user)
    active_todos = my_todos
    finished_todos = []
    return render(request, "player/home.html",
                  {'active_todos': active_todos,
                   'finished_todos': finished_todos})
