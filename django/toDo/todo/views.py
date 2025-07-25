from django.shortcuts import redirect, get_object_or_404, render
from .models import Task

# Create your views here.
def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def markasDone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def markasUndone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def editTask(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task' : get_task,
        }
        return render(request, 'edit_task.html',context)
    
def deleteTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')