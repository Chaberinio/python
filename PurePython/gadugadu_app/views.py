from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from gadugadu_app.forms import LoginForm
from gadugadu_app.models import Message


# Create your views here.

def ShowMessage(request):
    messages = Message.objects.all()
    return render(request, 'index.html', context={'messages': messages})

class ShowFormView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login_form.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data.get('login')
            password = form.cleaned_data.get('password')
            return HttpResponse(f'Zalogowano {login} twoje hasło {password}')
        else:
            return render(request, 'login_form.html', {'form': form})
