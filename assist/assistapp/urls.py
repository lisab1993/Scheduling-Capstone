from django.urls import path
from . import views

app_name = 'assistapp'
urlpatterns = [
    #Event related
    path('', views.my_events, name="my_events"),
    path('show_add_event/', views.show_add_event, name="show_add_event"),
    path('add_event/', views.add_event, name="add_event"),
    path('<int:pk>/delete_event/', views.delete_event, name="delete_event"),
    path('<int:pk>/edit_event/', views.edit_event, name="edit_event"),
    #EventTask related
    path('<int:event_id>/event_details', views.event_details, name="event_details"),
]
