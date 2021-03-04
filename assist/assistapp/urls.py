from django.urls import path
from . import views

app_name = 'assistapp'
urlpatterns = [
    path('', views.my_events, name="my_events"),
    path('<int:event_id>/', views.event_details, name="event_details"),
    path('show_add_event/', views.show_add_event, name="show_add_event"),
    path('add_event/', views.add_event, name="add_event"),
    path('<int:pk>/delete_event/', views.delete_event, name="delete_event")
]
