from django.urls import path
from . import views

urlpatterns = [
    path('task_solution/<int:task_id>/', views.TodecideView.as_view(), name='solution_of_task'),
]

