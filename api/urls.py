from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers

from .views import delete_view
router= routers.DefaultRouter()
router.register(r'clients', views.ClientViewSet)
router.register(r'project', views.ProjectViewSet)

urlpatterns = [    
    path('',include(router.urls))
    path('<id>/delete', delete_view ),
      
]

