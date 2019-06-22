from django.db import models

# Create your models here.

class Author(models.Model):
    fullName = models.CharField(max_length=250)

class Category(models.Model):
    categoryName = models.CharField(max_length=250)

