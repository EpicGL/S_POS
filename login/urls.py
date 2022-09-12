from django.urls import path, include
from . import views
from cashier.urls import urlpatterns as admin_parttenance
from kitchen.urls import urlpatterns as kitchen_parttenance
from waiter.urls import urlpatterns as waiter_parttenance

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('logout', views.logOut, name='logout'),
    path('admin/', include(admin_parttenance)),
    path('kitchen/', include(kitchen_parttenance)),
    path('waiter/', include(waiter_parttenance)),

]

