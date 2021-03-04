from django import forms
from .models import Event, EventTask


class EventForm(forms.ModelForm):
    date_time = forms.DateTimeField()

    class Meta:
        model = Event
        fields = ('title', 'start_date', 'end_date')
