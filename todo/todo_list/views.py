from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import *
from .models import *
# Create your views here.

def home(request):
    content = {
        'title' : 'Home'
    }
    return render(request, 'home.html', content)

def create(request):
    content = {
        'title' : 'Create Task'
    }
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        task = TodoList.objects.create(title=title, description=description, user=request.user)
        task.save()
        return redirect('my-task')
    return render(request, 'create.html', content)


def my_task(request):
    content = {
        'title' : 'My Task',
        'task' : TodoList.objects.filter(user=request.user)
    }
    return render(request, 'task.html', content)


def edit_task(request, id):
    task = TodoList.objects.get(id=id, completed=False)
    if request.method=="POST":
        task.title = request.POST['title']
        task.description = request.POST['description']
        completed = request.POST.get('completed', False) == 'on'
        task.completed = completed
        task.save()
        return redirect('my-task')

    return render(request, 'edit.html', {'title':'Edit Task','task':task})


def delete_task(request, id):
    try:
        task = get_object_or_404(TodoList,id=id)
        task.delete()
        return redirect('my-task')
    except Exception as a:
        print(a)
        return redirect('my-task')