# Name:
Assist

# Core functions:
* Daily Calendar
* Event Planner
* User System


# Daily Calendar:
* View all days in a standard calendar view
* Event name and time will be visible
* Calendar will come from Vuetify
* The Vuetify calendar will be accessed through an API call
* Most (if not all) of the calendar's functionality will be under created in the Vue app.


# Event Planner:
* Structured like a to do list
* User database will be included
* Clicking on "My Events" will show a list of events by name, ordered by their due date. 

* An event is the many, and the items are the one. 
* An event would be grocery shopping
* An item would be buying bread, going to the bank, get gas on the way.



# Models:
## Event
* event_title=models.CharField
* event_completed=models.Boolean
* event_start_date=models.DateTimeField
* event_due_date=models.DateTimeField

## Item
* item_name=models.CharField
* item_start_date=models.DateTimeField(auto_now_add=True)
* item_due_date=models.DateTimeField
* item_completed=models.Boolean
* item_priority=models.CharField(default='medium')
* item_notes=models.CharField
* item_images=models.ImageField

## Calendar
* tbd (after I look into the vuetify calendar, I will decide how this works
with models and then update this)


# Pages:
## login screen:
* The user is able to log in or sign up here.

## Calendar
* This will be treated like a home page
* When the user logs in, they will come straight here
* A vuetify calendar will be here for everyday use.
    
## My Events
* A list of all events will be here
* From here, we can add, edit, or delete events
* Events can be expanded using a collapsable
* When expanded, we can view and edit the due date and completion status
* When expanded, we can see all of the pictures for the event, with a
caption underneath stating which item it belongs to
* There will be a clear button leading to the detail page

## Event Detail Page
* At the top of the detail, we can manage the completion status,as well as the due date
* We can also add a note, mark the item as complete, delete it,
or manage pictures for the event 
* Going to manage pictures will allow
the user to add pictures as well

## Help Page: 
* The help page will have a small tutorial on how to use this site 
* Ideally, those with basic computer skills will be able to use this 
site, so the tutorial will be aimed at those who aren't comfortable
    

# Draw io Pictures
![Login](/images/capstone-login-draw.png)







