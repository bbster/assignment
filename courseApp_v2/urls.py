from django.urls import path, include

from courseApp_v2 import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.CourseViewSet)

urlpatterns = [
    path('', include(router.urls))
]

# urlpatterns = [
#     path('', views.CourseList.as_view()),
#     path('<int:pk>/', views.CourseDetail.as_view())
# ]