import pytest
from todos.models import *
from django.utils import timezone


@pytest.mark.django_db
def test_home_page(client):
    response = client.get('')

    assert 'Todo List' in response.content.decode('utf-8')


@pytest.mark.django_db
def test_add_todo(client):
    response = client.post('/todos/new/', {
        'title': '알고리즘 공부',
        'content': '알고리즘 문제 한 개 풀기'
    })

    assert Todo.objects.all().count() == 1
    todo = Todo.objects.get(id=1)

    assert todo.title == '알고리즘 공부'
    assert todo.content == '알고리즘 문제 한 개 풀기'

    assert response.status_code == 302
    assert response.url == '/'


@pytest.mark.django_db
def test_show_todo_list(client):
    Todo.objects.create(title="알고리즘 공부", content="알고리즘 문제 한 개 풀기")
    Todo.objects.create(title="치과가기")

    response = client.get('/')

    assert "알고리즘 공부" in response.content.decode('utf-8')
    assert "치과가기" in response.content.decode('utf-8')


@pytest.mark.django_db
def test_show_todo_title_after_adding(client):
    response = client.get('/')
    assert "알고리즘 공부" not in response.content.decode('utf-8')

    client.post('/todos/new/', {
        'title': '알고리즘 공부',
        'content': '알고리즘 문제 한 개 풀기',
    })

    response = client.get('/')
    assert "알고리즘 공부" in response.content.decode('utf-8')


@pytest.mark.django_db
def test_delete_todo(client):
    Todo.objects.create(title="알고리즘 공부", content="알고리즘 문제 한 개 풀기")
    Todo.objects.create(title="치과가기")

    todo = Todo.objects.get(title='치과가기')

    client.post('/todos/' + str(todo.id) + '/delete/')

    todos = Todo.objects.all()

    assert todos.count() == 1
    assert todos[0].title == '알고리즘 공부'


@pytest.mark.django_db
def test_check_if_todo_is_completed(client):
    todo = Todo.objects.create(title="치과가기")

    assert todo.isCompleted is False

    client.post('/todos/' + str(todo.id) + '/edit-check', {
        'isCompleted': 'on'
    })

    edited_todo = Todo.objects.get(id=todo.id)
    assert edited_todo.isCompleted is True

    client.post('/todos/' + str(todo.id) + '/edit-check')

    edited_todo = Todo.objects.get(id=todo.id)
    assert edited_todo.isCompleted is False


@pytest.mark.django_db
def test_enable_to_pick_deadline(client):
    client.post('/todos/new/', {
        'title': '알고리즘 공부',
        'content': '알고리즘 문제 한 개 풀기',
        'deadline': '2018-11-04 23:59:59'
    })

    todo = Todo.objects.get(title='알고리즘 공부')
    assert todo.deadline.year == 2018
    assert todo.deadline.month == 11
    assert todo.deadline.day == 4
    assert todo.deadline.hour == 23
    assert todo.deadline.minute == 59
    assert todo.deadline.second == 59


@pytest.mark.django_db
def test_edit_todo(client):
    Todo.objects.create(title="알고리즘 공부", content="알고리즘 문제 한 개 풀기", deadline="2018-11-04 23:59:59")

    client.post('/todos/1/edit/', {
        'title': '알고리즘 시험 준비',
        'content': '알고리즘 시험 준비하기'
    })

    todo = Todo.objects.get(id=1)

    assert todo.title == '알고리즘 시험 준비'
    assert todo.content == '알고리즘 시험 준비하기'


@pytest.mark.django_db
def test_show_todo_missed_deadline(client):
    cur_time = timezone.now()

    Todo.objects.create(title="치과 가기", deadline=cur_time + timezone.timedelta(days=3))
    response = client.get('/')
    assert '마감' not in response.content.decode('utf-8')

    Todo.objects.create(title="알고리즘 공부", content="알고리즘 문제 한 개 풀기", deadline=cur_time - timezone.timedelta(days=3))
    response = client.get('/')
    assert '마감' in response.content.decode('utf-8')


@pytest.mark.django_db
def test_set_priority_when_todo_is_added(client):
    client.post('/todos/new/', {'title': 'todo1', 'content': ''})
    client.post('/todos/new/', {'title': 'todo2', 'content': ''})
    client.post('/todos/new/', {'title': 'todo3', 'content': ''})

    assert Todo.objects.get(title='todo1').priority == 1
    assert Todo.objects.get(title='todo2').priority == 2
    assert Todo.objects.get(title='todo3').priority == 3


@pytest.mark.django_db
def test_change_priority(client):
    client.post('/todos/new/', {'title': 'todo1', 'content': ''})
    client.post('/todos/new/', {'title': 'todo2', 'content': ''})
    client.post('/todos/new/', {'title': 'todo3', 'content': ''})
    client.post('/todos/new/', {'title': 'todo4', 'content': ''})

    client.post('/todos/edit-priority/', {
        'upTodoId': '4',
        'baseTodoId': '2'
    })

    assert Todo.objects.get(title='todo1').priority == 1
    assert Todo.objects.get(title='todo2').priority == 3
    assert Todo.objects.get(title='todo3').priority == 4
    assert Todo.objects.get(title='todo4').priority == 2

    client.post('/todos/edit-priority/', {
        'upTodoId': '2',
        'baseTodoId': '1'
    })

    assert Todo.objects.get(title='todo1').priority == 2
    assert Todo.objects.get(title='todo2').priority == 1
    assert Todo.objects.get(title='todo3').priority == 4
    assert Todo.objects.get(title='todo4').priority == 3

    client.post('/todos/new/', {'title': 'todo5', 'content': ''})

    assert Todo.objects.get(title='todo5').priority == 5


@pytest.mark.django_db
def test_change_priority_after_todo_is_deleted(client):
    client.post('/todos/new/', {'title': 'todo1', 'content': ''})
    client.post('/todos/new/', {'title': 'todo2', 'content': ''})
    client.post('/todos/new/', {'title': 'todo3', 'content': ''})
    client.post('/todos/new/', {'title': 'todo4', 'content': ''})

    client.post('/todos/2/delete/')

    assert Todo.objects.get(title='todo1').priority == 1
    assert Todo.objects.get(title='todo3').priority == 2
    assert Todo.objects.get(title='todo4').priority == 3
