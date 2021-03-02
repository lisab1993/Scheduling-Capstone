from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .models import Event, EventTask, Priority


#DON'T FORGET TO CHANGE THE HOMEPAGE TO CALENDAR VIEW
#MY_EVENTS IS BEING USED AS A PLACEHOLDER AS IT'S BEING BUILT FIRST
def my_events(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'assistapp/my_events.html', context)


    