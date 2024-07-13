from django.urls import path, include

from .views import TaskAPIView

urlpatterns = [
    path('task', TaskAPIView.as_view()),
    path('task/<int:pk>', TaskAPIView.as_view()),
]