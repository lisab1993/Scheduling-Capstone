from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'assistapp'
urlpatterns = [
    #Event related
    path('', views.my_events, name="my_events"),
    path('show_add_event/', views.show_add_event, name="show_add_event"),
    path('add_event/', views.add_event, name="add_event"),
    path('<int:pk>/delete_event/', views.delete_event, name="delete_event"),
    path('<int:pk>/show_edit_event/', views.show_edit_event, name="show_edit_event"),
    path('<int:pk>/edit_event/', views.edit_event, name="edit_event"),
    path('show_past_events/', views.show_past_events, name="show_past_events"),
    #EventTask related
    path('<int:event_id>/task_list', views.task_list, name="task_list"),
    path('<int:event_id>/show_add_task/', views.show_add_task, name="show_add_task"),
    path('<int:event_id>/add_task/', views.add_task, name="add_task"),
    path('<int:pk>/delete_task/', views.delete_task, name="delete_task"),
    path('<int:id>/show_edit_task/', views.show_edit_task, name="show_edit_task"),
    path('<int:id>/edit_task/', views.edit_task, name="edit_task"),
    #Calendar related
    path('show_calendar/', views.show_calendar, name="show_calendar"),
    path('get_events/', views.get_events, name="get_events"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

