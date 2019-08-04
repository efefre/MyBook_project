from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book, Author, Category
from .utils import save_in_database
import requests

# Create your views here.
def index(request):
    books = Book.objects.order_by('title')

    context = {
        'books':books
    }
    return render(request, 'books/home.html', context)

def add_book(request):
    return render(request, 'books/add_book.html')

def new_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        category = request.POST['category']
        description = request.POST['description']
        averageRaitnig = request.POST['averageRaitnig']
        link = request.POST['link']

        save_in_database(request, author, title, category, description, averageRaitnig, link)

    return redirect('/add')

def search(request):
    books = Book.objects.order_by('title')

    # Title
    if 'title' in request.GET:
        title = request.GET['title']

        if title:
            books = books.filter(title__icontains=title)

    # Author
    if 'author' in request.GET:
        author = request.GET['author']

        if author:
            books = books.filter(author__fullName__icontains=author)

    #Category
    if 'category' in request.GET:
        category = request.GET['category']

        if category:
            books = books.filter(category__categoryName__icontains=category)


    context = {
        'books':books,
    }

    return render(request, 'books/search.html', context)

def find_book_in_google_books(request):
    if request.method == 'POST':
        q = request.POST['textstring']
        title = request.POST['title']
        author = request.POST['author']


        if title:
            api_url = 'https://www.googleapis.com/books/v1/volumes?q={}+intitle:{}'.format(q, title)
            if author:
                api_url = 'https://www.googleapis.com/books/v1/volumes?q={}+intitle:{}+inauthor:{}'.format(q, title, author)
        elif author:
            api_url = 'https://www.googleapis.com/books/v1/volumes?q={}+inauthor:{}'.format(q, author)
        else:
            api_url = 'https://www.googleapis.com/books/v1/volumes?q={}'.format(q)

        response = requests.get(api_url)
        data_from_google_books = response.json()
        total_items = data_from_google_books['totalItems']
        if total_items > 0:
            books = data_from_google_books['items']

            context = {
                'books':books,
                'total_items':total_items
            }

            return render(request, 'books/add_book_from_google_api.html', context)
    messages.error(request, 'Nie udało się znaleźć książki w Google Books. Możesz ją dodać przez formularz')
    return redirect('/add')

def save_book_from_google_in_db(request):
    if request.method == 'POST':
        checked_books_id = request.POST.getlist('checked-book-id')

        for book_id in checked_books_id:
            book_url = 'https://www.googleapis.com/books/v1/volumes/{}'.format(book_id)
            response = requests.get(book_url)
            book_detail = response.json().get('volumeInfo')
            title = book_detail.get('title')
            author = book_detail.get('authors')
            if len(author) > 1:
                authors = ''
                for name in author:
                    authors = authors +' ' + name
                author = authors
            else:
                author = author[0]
            category = book_detail.get('categories')
            if category:
                if len(category) > 1:
                    categories = ''
                    for name in category:
                        categories = categories + name
                    category = categories
                else:
                    category = category[0]
            description = book_detail.get('description')
            averageRaitnig = book_detail.get('averageRating')
            link = book_detail.get('canonicalVolumeLink')
            print(author)
            save_in_database(request, author, title, category, description, averageRaitnig, link)

    return redirect('/add')