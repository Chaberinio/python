from django.db import models

# Create your models here.
class Platform(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.name}'

class Game(models.Model):
    star = '★'
    empty_star = '☆'
    RatingChoices = (
        (1, star + empty_star*9),
        (2, star * 2 + empty_star * 8),
        (3, star * 3 + empty_star * 7),
        (4, star * 4 + empty_star * 6),
        (5, star * 5 + empty_star * 5),
        (6, star * 6 + empty_star * 4),
        (7, star * 7 + empty_star * 3),
        (8, star * 8 + empty_star * 2),
        (9, star * 9 + empty_star * 1),
        (10, star * 10),
    )
    name = models.CharField(max_length=128)
    description = models.TextField()
    rating = models.IntegerField(choices=RatingChoices)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    platform = models.ForeignKey('Platform', on_delete=models.CASCADE, null=True, blank=True)
    category = models.ManyToManyField('Category', blank=True)

    def __str__(self):
        return f'{self.name} {self.description} {self.rating} {self.price} {self.platform}'

class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.name}'

class GameDetails(models.Model):
    cheat_codes = models.CharField(max_length=512, blank=True)
    finished = models.BooleanField()
    play_time = models.DurationField()
    game = models.OneToOneField(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.cheat_codes} ukończono: {self.finished}, czas gry: {self.play_time}'

