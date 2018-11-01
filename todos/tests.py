import pytest

from todos.models import *


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

    assert response.json()['result'] == 'True'
