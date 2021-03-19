
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('assistapp.urls')),
    path('users/', include('users.urls')),
]
