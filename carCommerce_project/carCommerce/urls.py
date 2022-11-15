from django.contrib import admin
from django.urls import path
import carComm_app.views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', carComm_app.views.home, name = 'home'),
    path('', carComm_app.views.home, name = 'home'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
