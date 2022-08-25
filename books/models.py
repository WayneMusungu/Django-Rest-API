from django.db import models

# Create your models here.

class Books(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    summary = models.TextField()
    genre = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    
    def __str__(self):
        return (f'{self.name} by {self.author}')
    
