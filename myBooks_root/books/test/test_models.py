from ..models import Author, Category
import pytest
from mixer.backend.django import mixer

@pytest.mark.django_db
def test_create_author():
    author = Author.objects.create(fullName="Gall Anonim")
    author.save()
    assert author.fullName == "Gall Anonim"

@pytest.mark.django_db
def test_create_category():
    category = Category.objects.create(categoryName="Pierwsza kategoria")
    category.save()
    assert category.categoryName == "Pierwsza kategoria"

@pytest.mark.django_db
def test_create_book():
    author = Author.objects.create(fullName="Gall Anonim")
    author.save()
    category = Category.objects.create(categoryName="Pierwsza kategoria")
    category.save()
    book = mixer.blend('books.Book', category = category, author = author, title="Książka testowa")
    assert book.title == "Książka testowa"
