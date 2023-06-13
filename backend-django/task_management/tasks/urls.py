from django.urls import path

from .views import AllTasksView, CreateTasksView, UpdateTaskView

urlpatterns = (
    path('', AllTasksView.as_view(), name='all tasks'),
    path('create/', CreateTasksView.as_view(), name='create task'),
    path('update/<int:id>', UpdateTaskView.as_view(), name='update task')
)