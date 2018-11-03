from django.shortcuts import render, redirect


from todos.models import *


def home(request):
    todos = Todo.objects.all()

    return render(request, 'home.html', {'todos': todos})


def new_todo(request):
    Todo.objects.create(title=request.POST['title'], content=request.POST['content'])
    return redirect('/')


def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return redirect('/')


def edit_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if 'isCompleted' in request.POST:
        todo.isCompleted = True if request.POST.get('isCompleted') == 'on' else False

    todo.save()
    return redirect('/')
