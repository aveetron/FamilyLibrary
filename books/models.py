from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class LibraryLocation(models.Model):
    name = models.CharField( max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    photo = models.ImageField(upload_to='uploads/',default='static/assets/img/cabin.png')
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    location = models.ForeignKey(LibraryLocation, on_delete=models.CASCADE)
    in_stock = models.BooleanField()

    def __str__(self):
        return self.name
    
    

