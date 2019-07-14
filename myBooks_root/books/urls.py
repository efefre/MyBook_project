from django.urls import path
from . import views


app_name="books"

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add', views.add_book, name ='add_book'),
    path('new-book', views.new_book, name='new_book'),
    path('search', views.search, name='search'),
    path('add-book-from-google-books', views.add_book_from_google_books, name='add_book_from_google'),
]
