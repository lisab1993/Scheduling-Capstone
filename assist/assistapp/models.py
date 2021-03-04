from django.db import models
from django.contrib.auth.models import User
from datetime import datetime    

# Create your models here.

class Priority(models.Model):
    urgency = models.CharField(max_length=100)

    def __str__(self):
        return self.urgency
    

class Event(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField(default=datetime.now())
    end_date = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name ='events')

    def __str__(self):
        return self.title
    

class EventTask(models.Model):
    name = models.CharField(max_length=255)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_tasks')
    due_date = models.DateTimeField(default=datetime.now())
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT, related_name='event_tasks', null=True)
    notes = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name + ' - ' + self.event.title
    

