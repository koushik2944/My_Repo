from django.urls import path
from .import views

urlpatterns = [
    # Add Task
    path('addTask/',views.addTask,name='addTask'),
    # Mark as Done
    path('markas_done/<int:pk>',views.markasDone, name='markas_done'),
    # Mark as Undone
    path('markas_undone/<int:pk>',views.markasUndone, name='markas_undone'),
    # Edit Task
    path('editTask/<int:pk>/',views.editTask, name='editTask'),
    # Delete Task with id
    path('deleteTask/<int:pk>', views.deleteTask, name='deleteTask'),
]