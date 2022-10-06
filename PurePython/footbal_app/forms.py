from cProfile import label

from django import forms

from firstapp.views import Game
from footbal_app.models import Team


class FootballForm(forms.ModelForm):
    class Meta:
        model = Game

        hostTeam = forms.ChoiceField(queryset=Team.objects.all())
        hostScore = forms.IntegerField()
        guestScore = forms.IntegerField()
        guestTeam = forms.ChoiceField(queryset=Team.objects.all())

