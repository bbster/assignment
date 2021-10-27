from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('passengers/', include('passengerApp.urls')),
    path('courses/', include('courseApp.urls'))
]
