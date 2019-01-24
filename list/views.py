# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import List
from .forms import ItemForm, ListForm


@login_required
def todo_show(request, id):
    todo = get_object_or_404(List, pk=id)
    context = {'list': todo}

    if todo.owner == request.user:
        context['form'] = ItemForm()
    return render(request,
                  'list/todo_show.html',
                  context,
                  )


@login_required
def add_task(request, id):
    todo = get_object_or_404(List, pk=id)
    if not todo.owner == request.user:
        raise PermissionDenied

    task = todo.new_item()
    form = ItemForm(request.POST)
    if form.is_valid():
        task.list = todo
        task.name = form.cleaned_data['name']
        task.save()

    return redirect("list_todo_show", id)


@login_required
def todo_delete(request, id):
    todo = get_object_or_404(List, pk=id)
    if not todo.owner == request.user:
        raise PermissionDenied
    todo.delete()
    return redirect('player_home')


@login_required
def add_todo(request):
    form = ListForm(request.POST)
    if form.is_valid():
        todo = List.objects.create(
            name=form.cleaned_data['name'],
            owner=request.user,
        )
        todo.save()
    return redirect('player_home')
