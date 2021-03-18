from django.contrib import admin
from .models import Event, EventTask

# Register your models here.
admin.site.register(Event)
admin.site.register(EventTask)