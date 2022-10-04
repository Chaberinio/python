"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from firstapp.views import Hello, HelloName, Add, Multiply, Brothers, Fibbo, Game, HelloPath, Article, Greetings, Calc, \
    RandomGenerator, Index, Form, FizzBuzz, MultiplyTemplate, RpgGame, ListComments, Main, Login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index),
    path('helloname/<str:name>', HelloPath),
    path('add/', Add),
    path('multiply/<int:n>', Multiply),
    path('brothers/', Brothers),
    path('fibbo/', Fibbo),
    path('game/', Game),
    path('article/<int:id>', Article),
    path('greetings/<str:name>/<int:num>/', Greetings),
    path('calc/<int:numA>/<str:operation>/<int:numB>', Calc),
    path('randomGenerator/<int:min>/<int:max>', RandomGenerator),
    path('randomGenerator/<int:min>/<int:max>/<int:throws>', RandomGenerator),
    path('form/', Form),
    path('fizzBuzz/<int:n>', FizzBuzz),
    path('multiplyTemplate/<int:n>', MultiplyTemplate),
    path('multiplyTemplate/', MultiplyTemplate),
    path('rpgGame/', RpgGame),
    path('fakeComments/', ListComments),
    path('main/', Main),
    path('login/', Login)
]
