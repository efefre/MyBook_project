from django.db import models

# Create your models here.

class Author(models.Model):
    fullName = models.CharField(max_length=250)

class Category(models.Model):
    categoryName = models.CharField(max_length=250)

class Book(models.Model):
    title = models.CharField(max_length=500)
    author = models.ManyToManyField(Author)
    category = models.ManyToManyField(Category)
    description = models.TextField(blank=True)
    averageRaiting = models.DecimalField(max_digits=3, decimal_places=1)
    canonicalVolumeLink = models.CharField(max_length=250)
