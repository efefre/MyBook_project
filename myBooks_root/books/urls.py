from django.urls import path
from . import views


app_name="books"

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add', views.add_book, name ='add_book'),
    path('new-book', views.new_book, name='new_book'),
    path('search', views.search, name='search'),
]
