from django.contrib import admin
from .models import Priority, Event, EventTask

# Register your models here.
admin.site.register(Priority)
admin.site.register(Event)
admin.site.register(EventTask)