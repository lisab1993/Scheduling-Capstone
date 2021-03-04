from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .models import Event, EventTask, Priority
from django.contrib.auth.models import User
from .forms import EventForm


# DON'T FORGET TO CHANGE THE HOMEPAGE TO CALENDAR VIEW
# MY_EVENTS IS BEING USED AS A PLACEHOLDER AS IT'S BEING BUILT FIRST
# STILL NEED TO ADD SECURITY SO USERS ONLY SEE THEIR OWN STUFF


@login_required
def my_events(request):
    # only allow users to see their own events
    user = authenticate(username=request.user, password=request.user)
    logged_in = request.user
    user_events = Event.objects.filter(user=logged_in)
    form=EventForm()
    # put it in the context object to render on the my_events page
    context = {
        'user_events': user_events,
        'form':form
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
    

# warnings.warn("DateTimeField %s received a naive datetime (%s)"
# C:\Users\Lisa\AppData\Local\Programs\Python\Python39\lib\site-packages\django\db\models\fields\__init__.py:1367: RuntimeWarning: DateTimeField Event.end_date received a naive datetime (2021-03-04 17:44:00) while time zone support is active.





# def add_event(request):
#     if request.method == 'POST':
#         form = EventForm(request.POST)
#         if form.is_valid():
#             event = form.save(commit=False)
#             event.user = request.user
#             event.save()
#             return redirect('assistapp:my_events')
#     else:
#         form=EventForm()
#     return render(request, 'assistapp/my_events.html', {'form':form})

