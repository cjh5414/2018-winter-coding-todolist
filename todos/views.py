from django.http import JsonResponse
from django.shortcuts import render


from todos.models import *


def home(request):
    return render(request, 'home.html')


def create(request):
    Todo.objects.create(title=request.POST['title'], content=request.POST['content'])
    return JsonResponse({'result': 'True'})

