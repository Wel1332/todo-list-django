from django.shortcuts import render, redirect
from .models import Task

def home(request):
    tasks = Task.objects.all().order_by('-created')
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('home')
    return render(request, 'tasks/home.html', {'tasks': tasks})

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('home')

def delete_task(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect('home')
