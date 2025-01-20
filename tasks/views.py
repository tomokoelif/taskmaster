from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    todo_tasks = Task.objects.filter(completed=False).order_by('due_date')
    done_tasks = Task.objects.filter(completed=True).order_by('due_date')
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm()
    context = {
        'todo_tasks': todo_tasks,
        'done_tasks': done_tasks,
        'form': form,
    }
    return render(request, 'tasks/index.html', context)