from django.contrib import admin
from django.urls import path

from project import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', views.TaskListAPIView.as_view()),
    path('task_detail/', views.TaskDetailAPIView.as_view()),
]
