from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def home(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('/')
    return render(request, 'home.html', {'tasks': tasks})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/')

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('/')