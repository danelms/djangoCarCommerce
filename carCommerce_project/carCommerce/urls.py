from django.contrib import admin
from django.urls import path
import carComm_app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', carComm_app.views.home, name = 'home'),
    path('', carComm_app.views.home, name = 'home'),
]
