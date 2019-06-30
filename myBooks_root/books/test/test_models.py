from ..models import Author, Category
import pytest

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
