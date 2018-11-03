from django.urls import path, re_path

from . import views

app_name = 'todos'
urlpatterns = [
    path('new/', views.new_todo, name='todo_new'),
    re_path(r'^(?P<todo_id>\d+)/delete/', views.delete_todo, name='todo_delete'),
    re_path(r'^(?P<todo_id>\d+)/edit/check', views.edit_todo_check, name='todo_edit_check')
]
