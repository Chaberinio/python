from tkinter import CASCADE

from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=256)
    artist = models.ManyToManyField('Artist')

    def __str__(self):
        return f'{self.title} {self.artist}'

class Artist(models.Model):
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256, blank=True, null=True, default='')

    def __str__(self):
        return f'{self.name} {self.surname}'
