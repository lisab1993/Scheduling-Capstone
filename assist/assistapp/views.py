from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .models import Event, EventTask, Priority
from django.contrib.auth.models import User


# DON'T FORGET TO CHANGE THE HOMEPAGE TO CALENDAR VIEW
# MY_EVENTS IS BEING USED AS A PLACEHOLDER AS IT'S BEING BUILT FIRST
# STILL NEED TO ADD SECURITY SO USERS ONLY SEE THEIR OWN STUFF

## Event-related views
@login_required
def my_events(request):
    '''Displays all events for a user'''
    user = authenticate(username=request.user, password=request.user)
    logged_in = request.user
    user_events = Event.objects.filter(user=logged_in)
    # put it in the context object to render on the my_events page
    context = {
        'user_events': user_events,
        }
    return render(request, 'assistapp/my_events.html', context)


@login_required
def show_add_event(request):
    '''Renders the template to add an event'''
    return render(request, 'assistapp/add_event.html')

@login_required
def add_event(request):
    '''Saves a new event'''
    if request.method == 'POST':
        title = request.POST['title']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        user = request.user
        event = Event(title=title, start_date=start_date, end_date=end_date, user=user)
        event.save()
        return redirect('assistapp:my_events')
    

def delete_event(request, pk):
    '''Delete an event and it's tasks'''
    event = get_object_or_404(Event, pk=pk)
    if event.user != request.user:
        raise Http404
    event.delete()
    return redirect('assistapp:my_events')

def show_edit_event(request,pk):
    '''Renders the template to edit an event'''
    event = get_object_or_404(Event, pk=pk)
    if event.user != request.user:
        raise Http404
    return render(request, 'assistapp/edit_events.html', {'event':event})

def edit_event(request, pk):
    '''Saves changes made to an existing event'''
    event = get_object_or_404(Event, pk=pk)
    if event.user != request.user:
        raise Http404
    if request.method == 'POST':
        event.title = request.POST['title']
        event.start_date = request.POST['start_date']
        event.end_date = request.POST['end_date']
        event.user = request.user 
        event.save()
    return redirect('assistapp:my_events')



## EventTask-related views
@login_required
def task_list(request, event_id):
    '''A list of tasks for a specific event'''
    event = Event.objects.get(id=event_id)
    if event.user != request.user:
        raise Http404
    return render(request, 'assistapp/task_list.html', {'event': event})


@login_required
def show_add_task(request, event_id):
    '''Renders the template to add a task'''
    event = Event.objects.get(id=event_id)
    if event.user != request.user:
        raise Http404
    return render(request, 'assistapp/add_task.html', {'event':event})

@login_required
def add_task(request, event_id):
    '''Saves a new task to a specific event'''
    event = Event.objects.get(id=event_id)
    if event.user != request.user:
        raise Http404
    if request.method == 'POST':
        name = request.POST['name']
        event_id = event_id
        due_date = request.POST['due_date']
        priority_urgency = request.GET.get('priority_urgency')
        notes = request.POST['notes']
        image = request.FILES.get('image')
        event = EventTask(name=name, due_date=due_date, notes=notes, image=image, priority=priority_urgency, event_id=event_id)
        event.save()
        return HttpResponseRedirect(reverse('assistapp:task_list', args=[event_id]))


def delete_task(request, pk):
    '''Deletes a task'''
    task = get_object_or_404(EventTask, pk=pk)
    task.delete()
    #the request is going to include the page it came from
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
