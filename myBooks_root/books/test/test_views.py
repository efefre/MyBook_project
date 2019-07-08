from django.urls import reverse
from django.contrib.messages import get_messages
import pytest


book_for_test = {'title':'Python',
                 'author':'Junior Python',
                 'category':'',
                 'description':'',
                 'averageRaitnig':'',
                 'link':''}


@pytest.mark.django_db
def test_add_new_book_by_form(client):
    response = client.post(reverse('books:new_book'),
                           book_for_test)
    messages = [m.tags for m in get_messages(response.wsgi_request)]
    assert messages[0] == 'success'
