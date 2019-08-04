from django.urls import reverse, resolve

def test_index_url():
    path = reverse('books:index')
    assert resolve(path).url_name == 'index'
