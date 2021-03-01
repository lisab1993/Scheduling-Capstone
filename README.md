# Name:
Assist

# Core functions:
* daily calendar
* event planner
* user system


# Daily Calendar:
* view all days in a standard calendar view
* event name and time will be visible
* calendar will come from vuetify


# Event Planner:
* structured like a to do list
* user database will be included
* clicking on "My Events" will show a list of events by name, ordered by their due date. 

* An event is the many, and the items are the one. 
* An event would be grocery shopping
* An item would be buying bread, going to the bank, get gas on the way.



# Models:
## Event
* event_title (charfield)
* event_due_date (datetimefield)
* event_completed (boolean)

## Item
* item_name (charfield)
* item_due_date (datetimefield)
* item_completed (boolean)
* item_priority (charfield)(default to medium)
* item_notes (charfield)(no max char limit)
* item_images (imagefield)

## Calendar
* tbd (after I look into the vuetify calendar, I will decide how this works
with models and then update this)


# Pages:
## login screen:
    *able to log in or sign up here.

## Calendar
    *this will be treated like a home page
    * when the user logs in, they will come straight here
    * a vuetify calendar will be here for everyday use.
    
## My Events
    * a list of all events will be here
    * from here, we can add, edit, or delete events
    * events can be expanded using a collapsable
    * when expanded, we can view and edit the due date and completion status
    * when expanded, we can see all of the pictures for the event, with a
    caption underneath stating which item it belongs to
    * there will be a clear button leading to the detail page

## Event Detail Page
    * at the top of the detail, we can manage the completion status, as well as the due date
    * we can also add a note, mark the item as complete, delete it,
    or manage pictures for the event 
    * Going to manage pictures will allow
    the user to add pictures as well

## Help Page: 
    * the help page will have a small tutorial on how to use this site 
    * Ideally, those with basic computer skills will be able to use this 
    site, so the tutorial will be aimed at those who aren't comfortable
    








