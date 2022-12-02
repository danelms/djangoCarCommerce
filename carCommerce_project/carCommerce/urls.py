from django.contrib import admin
from django.urls import path
import carComm_app.views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', carComm_app.views.home, name = 'home'),
    path('', carComm_app.views.home, name = 'home'),
    path('listings/', carComm_app.views.listings, name = 'listings'),
    path('contact/', carComm_app.views.contact, name = 'contact'),
    path('carDetails/<str:registration>/', carComm_app.views.carDetails, name ='carDetails'),
    path('purchaseForm/<str:registration>/', carComm_app.views.purchaseForm, name = 'purchaseForm')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
