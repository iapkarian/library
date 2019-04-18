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
    number = models.CharField(max_length=20, blank=True, null=True)
    author = models.ForeignKey(Author)
    name = models.TextField(max_length=50)
    year = models.CharField(max_length=5)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    text = models.TextField()
    pages = models.IntegerField()
    genre = models.ManyToManyField(Genre)
    new = models.BooleanField(blank=True)

    def __str__(self):
        return self.name


class Readers(models.Model):
    user_number = models.IntegerField()
    first_name = models.TextField(max_length=10)
    secord_name = models.TextField(max_length=10)
    phone = models.CharField(max_length=15)
    address = models.TextField(max_length=50)
    email_address = models.EmailField()
    book_number = models.ManyToManyField(Book)

    def __str__(self):
        return self.secord_name


class Foresight(models.Model):
    number = models.IntegerField()
    text = models.TextField()
    author = models.ForeignKey(Author)
    book = models.ForeignKey(Book)

    def __str__(self):
        return self.number
