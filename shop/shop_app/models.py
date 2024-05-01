from bulk_update_or_create import BulkUpdateOrCreateQuerySet

from django.db import models


class Book(models.Model):
    objects = BulkUpdateOrCreateQuerySet.as_manager()

    name = models.CharField(max_length=255)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    pubdate = models.DateField()
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.pages} {self.price} {self.rating} {self.publisher} {self.pubdate}, {self.amount}"
