import pytest

from todos.models import *


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
        'content': '알고리즘 문제 한 개 풀기'
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
