from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'books/home.html')

def add_book(request):
    return render(request, 'books/add_book.html')
