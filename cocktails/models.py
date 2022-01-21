from django.db import models

# Create your models here.

class Cocktail(models.Model):
    ''' Cocktail Model '''
    name = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=250)
    recipe = models.TextField(max_length=1000)
    image = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'