from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    full_name = models.CharField(max_length=255)
    birth_year = models.PositiveSmallIntegerField(null=True, blank=True)
    address = models.CharField(default="Fergana")

    def __str__(self):
        return self.full_name


class Book(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    published_year = models.PositiveSmallIntegerField(default=2016)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title