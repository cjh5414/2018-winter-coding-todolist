import json

from django.http import JsonResponse
from todos.models import *


def create(request):
    Todo.objects.create(title=request.POST['title'], content=request.POST['content'])
    return JsonResponse({'result': 'True'})

