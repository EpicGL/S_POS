from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home,name='home'),
    path('login/', include('login.urls')),
    path('management/', include('cashier.urls')),
    path('waiter/', include('waiter.urls')),
    path('kitchen/', include('kitchen.urls')),

]


urlpatterns += static(settings. MEDIA_URL, document_root = settings.MEDIA_ROOT)