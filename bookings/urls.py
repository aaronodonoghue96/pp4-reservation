"""
URL configuration for restaurant_booking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.list_reservations, name='list_reservations'),
    path('create/', views.create_reservation, name='create_reservation'),
    path('update/<int:pk>/', views.update_reservation, name='update_reservation'),
    path('delete/<int:pk>/', views.delete_reservation, name='delete_reservation'),
    path('admin/', admin.site.urls),
]
