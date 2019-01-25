# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from list.models import List
from list.forms import ListForm
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy


@login_required()
def home(request):
    my_lists = List.objects.filter(owner=request.user)
    active_lists = my_lists.filter(is_finished=False)
    finished_lists = my_lists.difference(active_lists)

    form = ListForm()
    return render(request, "player/home.html",
                  {'active_todos': active_lists,
                   'finished_todos': finished_lists,
                   'form': form}
                  )


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "player/signup_form.html"
    success_url = reverse_lazy('player_home')
