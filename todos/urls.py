from django.urls import path

from . import views

urlpatterns = [
    path('new/', views.new_todo, name='todo_new')
]
