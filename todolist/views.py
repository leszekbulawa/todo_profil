from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'todolist/task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'todolist/task_detail.html', {'task': task})

def task_new(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_date = timezone.now()
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todolist/task_edit.html', {'form': form})

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.modified_date = timezone.now()
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todolist/task_edit.html', {'form': form})

def task_accept(request, pk):
    task = get_object_or_404(Task, pk=pk)
    #form = TaskForm(request.POST, instance=task)
    #task = form.save(commit=False)
    task.done_date = timezone.now()
    task.save()
    return redirect('task_list')

def task_remove(request, pk):
	task = get_object_or_404(Task, pk=pk)
	task.delete()
	return redirect('task_list')
