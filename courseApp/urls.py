from django.urls import path, include

from courseApp import views

urlpatterns = [
    path('', views.CourseList.as_view()),
    path('<int:pk>/', views.CourseDetail.as_view())
]
