from django.db import models


# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Game(models.Model):
    hostTeam = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='host_set')
    guestTeam = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='guest_set')
    hostScore = models.IntegerField()
    guestScore = models.IntegerField()

    def __str__(self):
        return f' Gospodarze: {self.hostTeam}, Wynik gospodarzy: {self.hostScore}, Goście: {self.guestTeam}, Wynik gości: {self.guestScore},'
