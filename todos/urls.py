from django.urls import path

from . import views

urlpatterns = [
    path('new/', views.create, name='todo_create')
]
