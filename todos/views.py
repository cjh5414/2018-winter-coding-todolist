from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_GET


from todos.models import *


@require_GET
def home(request):
    todos = Todo.objects.filter(isCompleted=False)
    completed_todos = Todo.objects.filter(isCompleted=True)

    return render(request, 'home.html', {'todos': todos, 'completed_todos': completed_todos})


@require_POST
def new_todo(request):
    Todo.objects.create(title=request.POST['title'], content=request.POST['content'])
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
