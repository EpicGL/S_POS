from . import views
from django.urls import path, include

urlpatterns = [
    
    path('',views.management, name='management'),
    path('inventory/',views.inventory, name='inventory'),
    path('sales/',views.sales, name='sales'),

    path('additem',views.add,name='additem'),
    path('edititem/<str:pk>/',views.edit,name='edititem'),
    path('deleteitem/<str:pk>/',views.deleteitem,name='deleteitem'),
    
]

