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
    path('<int:pk>/edit_event/', views.edit_event, name="edit_event"),
    #EventTask related
    path('<int:event_id>/event_details', views.event_details, name="event_details"),
    path('<int:event_id>/show_add_detail/', views.show_add_detail, name="show_add_detail"),
    path('<int:event_id>/add_detail/', views.add_detail, name="add_detail"),
    path('<int:pk>/delete_task/', views.delete_task, name="delete_task"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

