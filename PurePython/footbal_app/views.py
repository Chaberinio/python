from django.shortcuts import render
from django.views import View

from footbal_app.forms import FootballForm


# Create your views here.

class AddFootballMatch(View):
    def get(self, request):
        form = FootballForm()
        return render(request, 'footbal_app/add_football_match.html')