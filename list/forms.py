from django import forms
from .models import Item


class ItemForm(forms.Form):
    name = forms.CharField(label=False, help_text='New task', max_length=100)


class ListForm(forms.Form):
    name = forms.CharField(label=False, max_length=100)
