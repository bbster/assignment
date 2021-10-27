from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('passengers/', include('passengerApp.urls')),
    path('courses/', include('courseApp.urls')),
    path('courses_v2/', include('courseApp_v2.urls')),
    path('shop/', include('shoppingmallApp.urls'))
]
