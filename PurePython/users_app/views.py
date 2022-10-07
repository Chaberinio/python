from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from users_app.forms import LoginForm, RegisterUser


# Create your views here.
def create_user(request):
    user = User.objects.create_user(username='test',
                                    email='test@example.com',
                                     password='zaq1@WSX')
    return HttpResponse(f'Ok! {user.pk}')

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'user_app/login.html', {'form' : form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'),
                                password=form.cleaned_data.get('password'))
            print(form.cleaned_data.get('username'),form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                return HttpResponse('Ok! Autentyfikacja potwierdzona')
            else:
                return HttpResponse('Upsss! Nie ma cię w naszej bazie')
        else:
            return render(request, 'user_app/login.html', {'form': form})

class ImportantDataView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponse('Najlepsze kasztany są na placu Pigal')
        else:
            return HttpResponse('Tajne dane! Tylko dla zalogowanych!')

def MakeLogout(request):
    logout(request)
    return HttpResponse('Poprawne wylogowanie')



class RegisterView(View):
    def get(self, request):
        form = RegisterUser()
        return render(request, 'user_app/register.html', {'form': form})

    def post(self, request):
        try:
            form = RegisterUser(request.POST)
            if form.is_valid():
                user = User.objects.create_user(username=request.POST.get('username'),
                                           password=request.POST.get('password'),
                                           email=request.POST.get('email'))
                user.save()
                return redirect('/user/login/')
        except:
            return HttpResponse('Coś poszło nie tak')



