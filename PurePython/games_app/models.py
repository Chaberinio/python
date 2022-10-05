from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    rating = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.name} {self.description} {self.rating} {self.price}'
