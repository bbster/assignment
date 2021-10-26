from django.urls import path, include

from passengerApp import views

urlpatterns = [
    path('', views.passenger_list),
    path('<int:pk>/', views.passenger_detail)
]
