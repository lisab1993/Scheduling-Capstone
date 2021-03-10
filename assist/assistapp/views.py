from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .models import Event, EventTask, Priority
from django.contrib.auth.models import User


# DON'T FORGET TO CHANGE THE HOMEPAGE TO CALENDAR VIEW
# MY_EVENTS IS BEING USED AS A PLACEHOLDER AS IT'S BEING BUILT FIRST
# STILL NEED TO ADD SECURITY SO USERS ONLY SEE THEIR OWN STUFF

##Event-related views

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

def show_edit_event(request,pk):
    event = get_object_or_404(Event, pk=pk)
    if event.user != request.user:
        raise Http404
    return render(request, 'assistapp/edit_events.html', {'event':event})

def edit_event(request, pk):
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

# EventTask-related views

@login_required
def task_list(request, event_id):
    # return HttpResponse('detail page')
    # tasks = EventTask.objects.filter(event_id=event_id)
    # tasks = event.event_tasks.all()
    event = Event.objects.get(id=event_id)
    if event.user != request.user:
        raise Http404
    return render(request, 'assistapp/task_list.html', {'event': event})

@login_required
def show_add_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    if event.user != request.user:
        raise Http404
    return render(request, 'assistapp/add_detail.html', {'event':event})

@login_required
def add_detail(request, event_id):
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
    task = get_object_or_404(EventTask, pk=pk)
    task.delete()
    #the request is going to include the page it came from
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def show_edit_task(request, id):
    '''Render the template to edit a task'''
    # return HttpResponse("ok")
    task = get_object_or_404(EventTask, id=id)
    if task.event.user != request.user:
        raise Http404
    return render(request, 'assistapp/edit_task.html', {'task':task})


@login_required
def edit_task(request, id):
    task = get_object_or_404(EventTask, id=id)
    if task.event.user != request.user:
        raise Http404
    if request.method == 'POST':
        name = request.POST['name']
        due_date = request.POST['due_date']
        priority = request.POST['priority']
        notes = request.POST['notes']
        image = request.FILES.get('image')
        task = EventTask(name=name, due_date=due_date, notes=notes, image=image, priority=priority)
        task.save()
        #tell the program to return to the task list at the task's event id
        return redirect(request, 'assistapp:task_list', id='event_id')

    # path('<int:id>/edit_task/', views.edit_task, name="edit_task")

