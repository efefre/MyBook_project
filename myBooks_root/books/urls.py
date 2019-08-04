from django.urls import path
from . import views


app_name="books"

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add', views.add_book, name ='add_book'),
    path('new-book', views.new_book, name='new_book'),
    path('search', views.search, name='search'),
    path('find-book-in-google-books', views.find_book_in_google_books, name='find_book_in_google'),
    path('save-book-from-google-books', views.save_book_from_google_in_db, name='save_book_from_google'),
]
