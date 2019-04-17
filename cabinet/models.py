from django.db import models


class Author(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author)
    name = models.TextField(max_length=100)
    year = models.CharField(max_length=5)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    text = models.TextField()
    pages = models.IntegerField()
    genre = models.ForeignKey(Genre)

    def __str__(self):
        return self.name
