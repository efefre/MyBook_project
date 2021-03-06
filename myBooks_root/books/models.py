from django.db import models
from decimal import Decimal

# Create your models here.

class Author(models.Model):
    fullName = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.fullName

class Category(models.Model):
    categoryName = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.categoryName

class Book(models.Model):
    title = models.CharField(max_length=500)
    author = models.ManyToManyField(Author)
    category = models.ManyToManyField(Category, blank=True)
    description = models.TextField(blank=True)
    averageRaiting = models.DecimalField(max_digits=3, decimal_places=1, blank=True, default=Decimal(0.00))
    canonicalVolumeLink = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.title


