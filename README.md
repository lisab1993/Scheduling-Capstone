# Assist


* An event would be grocery shopping
* An item would be buying bread, going to the bank, get gas on the way.

## Functionality

- User management system (register, login, logout)
- Calendar of events users can edit
- Event planner with todo items

### Technologies Used

- Django (3.1)
- Python (3.9)
- Bootstrap (5)
- Vue.js + Vuetify

## Models:


### Priority
* urgency (CharField)

### Event

* title (CharField)
* start_date (DateTimeField)
* end_date (DateTimeField)
* user (ForeignKey to User)

### EventTask

* name (CharField)
* event (ForeignKey to Event)
* due_date (DateTimeField)
* priority (CharField(default='medium'))
* notes (TextField)
* image (ImageField)


## Pages:

### Login + Register
* Form for logging in (username, password)
* Form for registering (username, email, password)
* After logging in or registering, go to the calendar page

### Calendar
* List of events in a calendar (including event name and time)
* Calendar will come from [Vuetify](https://vuetifyjs.com/en/components/calendars/)
* This will be treated like a home page (when the user logs in, they will come straight here)
* Link to create a new event
    
### My Events
* List of events by name, ordered by their starting date
* From here, we can add, edit, or delete events
* There will be a clear button leading to the detail page

### Event Detail Page

* Structured like a todo list
* List of event tasks
  * View and edit the due date, completion status, picture, notes
  * Mark the task as complete, delete it

### Help Page
* The help page will have a small tutorial on how to use this site 
* Ideally, those with basic computer skills will be able to use this site, so the tutorial will be aimed at those who aren't comfortable


## Schedule

### Week 1

- Create the project and apps
- Create the models
- User management (register/login/logout)
- Event list (CRUD)

### Week 2

- Event detail (CRUD on EventTask)
- Styling
- Calendar

### Week 3

- Calendar
- Help page / tutorial

### Stretch

- Multiple images for an EventTask (separate model EventTaskImage)


