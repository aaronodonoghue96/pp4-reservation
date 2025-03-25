# restaurant_booking/urls.py
from django.contrib import admin
from django.urls import path, include  
# include is used to refer to the app-level URLs

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin page URL
    path('', include('bookings.urls')),  
    # Include the app-level URLs from the 'bookings' app
]
