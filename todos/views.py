from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_GET
from django.utils import timezone

from todos.models import *


@require_GET
def home(request):
    todos = Todo.objects.filter(isCompleted=False)
    completed_todos = Todo.objects.filter(isCompleted=True)

    for todo in todos:
        if todo.deadline is not None:
            if todo.deadline < timezone.now():
                todo.miss_deadline = True
            todo.deadline = todo.deadline.strftime("%Y-%m-%dT%H:%M")
    for todo in completed_todos:
        if todo.deadline is not None:
            todo.deadline = todo.deadline.strftime("%Y-%m-%dT%H:%M")

    return render(request, 'home.html', {'todos': todos, 'completed_todos': completed_todos})


@require_POST
def new_todo(request):
    datetime = None
    if 'deadline' in request.POST and request.POST['deadline'] != "":
        datetime = request.POST['deadline']
    Todo.objects.create(title=request.POST['title'], content=request.POST['content'], deadline=datetime)
    return redirect('/')


@require_POST
def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return redirect('/')


@require_POST
def edit_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.title = request.POST.get('title')
    todo.content = request.POST.get('content')
    datetime = None
    if 'deadline' in request.POST and request.POST['deadline'] != "":
        datetime = request.POST['deadline']
    todo.deadline = datetime
    todo.save()

    return redirect('/')


@require_POST
def edit_todo_check(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.isCompleted = True if 'isCompleted' in request.POST else False
    todo.save()

    return redirect('/')
