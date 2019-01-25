# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import List, Item
from .forms import ItemForm, ListForm


def todo_show(request, id):
    """Redirect to page with shown todo as list"""
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
        todo.is_finished = todo.get_is_finished()
        todo.save()
    return redirect("list_todo_show", id)


@login_required
def task_delete(request, id):
    """Delete task and redirect to todo list"""
    task = get_object_or_404(Item, pk=id)
    todo = task.list
    if not task.list.owner == request.user:
        raise PermissionDenied
    task.delete()
    todo.is_finished = todo.get_is_finished()
    todo.save()
    return redirect('list_todo_show', todo.id)


@login_required()
def task_change_status(request, id):
    """Changes status of task: In progress / Done"""
    task = get_object_or_404(Item, pk=id)
    todo = task.list
    if not task.list.owner == request.user:
        raise PermissionDenied
    task.is_finished = not task.is_finished
    task.save()
    todo.is_finished = todo.get_is_finished()
    todo.save()
    return redirect('list_todo_show', todo.id)


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
