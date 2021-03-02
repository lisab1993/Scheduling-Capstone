from django.urls import path
from . import views


app_name = 'users'
urlpatterns = [
    path('registration_page/', views.registration_page, name='registration_page'),
    path('register_user/', views.register_user, name='register_user'),
]
