from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .models import Event, EventTask, Priority
from django.contrib.auth.models import User


# DON'T FORGET TO CHANGE THE HOMEPAGE TO CALENDAR VIEW
# MY_EVENTS IS BEING USED AS A PLACEHOLDER AS IT'S BEING BUILT FIRST
# STILL NEED TO ADD SECURITY SO USERS ONLY SEE THEIR OWN STUFF


@login_required
def my_events(request):
    # only allow users to see their own events
    user = authenticate(username=request.user, password=request.user)
    logged_in = request.user
    user_events = Event.objects.filter(user=logged_in)
    # put it in the context object to render on the my_events page
    context = {
        'user_events': user_events,
        }
    return render(request, 'assistapp/my_events.html', context)



@login_required
def event_details(request, event_id):
    # return HttpResponse('detail page')
    tasks = EventTask.objects.filter(event_id=event_id)
    return render(request, 'assistapp/event_details.html', {'tasks':tasks})



@login_required
def show_add_event(request):
    return render(request, 'assistapp/add_event.html')

@login_required
def add_event(request):
    if request.method == 'POST':
        title = request.POST['title']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        user = request.user
        event = Event(title=title, start_date=start_date, end_date=end_date, user=user)
        event.save()
        return redirect('assistapp:my_events')
    

def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if event.user != request.user:
        raise Http404
    event.delete()
    return redirect('assistapp:my_events')





