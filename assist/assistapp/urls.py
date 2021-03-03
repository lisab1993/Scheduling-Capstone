from django.urls import path
from . import views

app_name = 'assistapp'
urlpatterns = [
    path('', views.my_events, name="my_events"),
    path('<int:event_id>/', views.event_details, name="event_details"),
]
