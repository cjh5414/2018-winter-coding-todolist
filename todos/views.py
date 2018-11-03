from django.http import JsonResponse
from django.shortcuts import render


from todos.models import *


def home(request):
    todos = Todo.objects.all()

    return render(request, 'home.html', {'todos': todos})


def new_todo(request):
    Todo.objects.create(title=request.POST['title'], content=request.POST['content'])
    return JsonResponse({'result': 'True'})

