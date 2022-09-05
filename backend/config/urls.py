from django.contrib import admin
from django.urls import path
from .apps.calculator import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ipoteca/', views.IpotekaViewSet.as_view({'get': 'list'}), name='ipoteca_list'),
]
