from django.db import models

# Create your models here.
from django.utils.timezone import now
from books.constants import JOURNAL_TYPES


class BookJournalBase(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=now, blank=True)


    class Meta:
        abstract = True


class Book(BookJournalBase):
    num_pages = models.IntegerField()
    genre = models.CharField(max_length=50)

class Journal(BookJournalBase):
    type = models.CharField(choices=JOURNAL_TYPES, default='BULLET', max_length=50, blank=True)
    publisher = models.CharField(max_length=150)