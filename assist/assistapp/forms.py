from django import forms
from .models import Event, EventTask, Priority


class PriorityChoiceField(forms.Form):

    priorities = forms.ModelChoiceField(
        queryset=Priority.objects.values_list()
    )
