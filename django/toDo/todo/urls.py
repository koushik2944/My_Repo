from django.urls import path
from .import views

urlpatterns = [
    path('addTask/',views.addTask,name='addTask'),
    path('markas_done/<int:pk>',views.markasDone, name='markas_done'),
    path('markas_undone/<int:pk>',views.markasUndone, name='markas_undone'),
]