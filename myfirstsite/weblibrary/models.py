from django.db import models
from django.utils import timezone
# Create your models here.


class BookList(models.Model):
    name = models.CharField(max_length=200)

    def publish(self):
        self.add_book()
        self.del_book()
        self.save()

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=2)

