from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book, Author, Category

# Create your views here.
def index(request):
    books = Book.objects.all()

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

        if not averageRaitnig:
            averageRaitnig = 0.0

        book = Book(title=title,
                    description=description,
                    averageRaiting=averageRaitnig,
                    canonicalVolumeLink=link)

        category_in_database = Category.objects.all().filter(categoryName=category).values('id')

        if category_in_database:
            category = category_in_database[0]['id']
        else:
            category = Category.objects.create(categoryName=category)


        # Check if author exist in database
        author_in_database = Author.objects.all().filter(fullName=author).values('id')

        if author_in_database:
            author = author_in_database[0]['id']
            book_in_database = Book.objects.all().filter(title=title, author=author)

            # Check if book exist in database
            if book_in_database:
                messages.error(request, 'Książka istnieje w bazie danych')
                return redirect('/add')
            else:
                book.save()
                book.category.add(category)
                book.author.add(author)

                messages.success(request, 'Książka została dodana do bazy danych. Możesz dodać kolejną książkę :)')
                return redirect('/add')
        else:
            book.save()
            author = Author.objects.create(fullName=author)
            book.author.add(author)
            book.category.add(category)

            messages.success(request, 'Książka została dodana do bazy danych. Możesz dodać kolejną książkę :)')
            return redirect('/add')