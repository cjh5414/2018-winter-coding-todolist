from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_GET
from django.utils.dateparse import parse_datetime
import pytz

from todos.models import *


@require_GET
def home(request):
    todos = Todo.objects.filter(isCompleted=False)
    completed_todos = Todo.objects.filter(isCompleted=True)

    return render(request, 'home.html', {'todos': todos, 'completed_todos': completed_todos})


@require_POST
def new_todo(request):
    datetime = None
    if 'deadline' in request.POST and request.POST['deadline'] != "":
        # datetime = pytz.timezone("Asia/Seoul").localize(parse_datetime(request.POST.get('deadline')))
        datetime = request.POST['deadline']
    Todo.objects.create(title=request.POST['title'], content=request.POST['content'], deadline=datetime)
    return redirect('/')


@require_POST
def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return redirect('/')


@require_POST
def edit_todo_check(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.isCompleted = True if 'isCompleted' in request.POST else False
    todo.save()

    return redirect('/')
