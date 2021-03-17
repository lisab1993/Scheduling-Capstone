from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Priority(models.Model):
    urgency = models.CharField(max_length=100)

    def __str__(self):
        return self.urgency
    

class Event(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name ='events')

    def __str__(self):
        return self.title
    

class EventTask(models.Model):
    name = models.CharField(max_length=255)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tasks')
    due_date = models.DateTimeField(default=timezone.now)
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT, related_name='tasks', null=True)
    notes = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' - ' + self.event.title
    

