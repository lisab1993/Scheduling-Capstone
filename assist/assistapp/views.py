from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .models import Event, EventTask, Priority


# DON'T FORGET TO CHANGE THE HOMEPAGE TO CALENDAR VIEW
# MY_EVENTS IS BEING USED AS A PLACEHOLDER AS IT'S BEING BUILT FIRST
@login_required
def my_events(request):
    # only allow users to see their own events
    user = authenticate(username=request.user, password=request.user)
    logged_in = request.user
    user_events = Event.objects.filter(user=logged_in)

    # put it in the context object to render on the my_events page
    context = {
        'user_events': user_events
    }
    return render(request, 'assistapp/my_events.html', context)


@login_required
def event_details(request, event_id):
    # return HttpResponse('detail page')
    tasks = EventTask.objects.filter(event_id=event_id)

    return render(request, 'assistapp/event_details.html', {'tasks':tasks})



#event_id refers to which event the task belongs to.
#it also needs to get passed into the urls