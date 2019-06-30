from ..models import Author
import pytest

@pytest.mark.django_db
def test_create_author():
    author = Author.objects.create(fullName="Gall Anonim")
    author.save()
    assert author.fullName == "Gall Anonim"
