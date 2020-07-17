from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    in_stock = models.BooleanField()

    def __str__(self):
        return self.name
    
    