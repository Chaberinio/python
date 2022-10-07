from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from football_app.forms import FootballForm
from football_app.models import Game


# Create your views here.

class AddFootballView(View):
    def get(self, request):
        form = FootballForm()
        return render(request,
                      'football_app/football_game.html',
                      {'form': form})

    def post(self, request):
        form = FootballForm(request.POST, instance=Game())
        if form.is_valid():
            if form.cleaned_data.get('hostTeam') == form.cleaned_data.get('sguestTeam'):
                return render(request,
                              'football_app/football_game.html',
                              {'form': form,
                               'message': "Drużyny nie mogą być takie same"})
            if form.cleaned_data.get('hostScore') < 0 or form.cleaned_data.get('guestScore') < 0:
                return render(request,
                              'football_app/football_game.html',
                              {'form': form,
                               'message': "Wynik nie może być ujemny"})
            form.save()
            return redirect('/football/game/')
        else:
            return render(request,
                          'football_app/football_game.html',
                          {'form': form})