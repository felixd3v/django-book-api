from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=250)
    category = models.CharField(max_length=80)
    author = models.CharField(max_length=250)
    price = models.CharField(max_length=12)

    def __str__(self):
        return self.name

