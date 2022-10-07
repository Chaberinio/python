from cProfile import label

from django import forms


from football_app.models import Team, Game


class FootballForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

