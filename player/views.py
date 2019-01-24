# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from list.models import List
from list.forms import ListForm
# Create your views here.


@login_required()
def home(request):
    my_lists = List.objects.filter(owner=request.user)
    active_lists = my_lists
    finished_lists = []

    form = ListForm()
    return render(request, "player/home.html",
                  {'active_todos': active_lists,
                   'finished_todos': finished_lists,
                   'form': form}
                  )

