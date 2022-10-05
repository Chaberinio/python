from django.shortcuts import render, redirect

from games_app.models import Game


# Create your views here.

def Show(request):
    games  = Game.objects.all()
    return render(request, 'showGame.html', {'games': games})

def ShowGameByID(request, pk):
    games = Game.objects.get(pk=pk)
    return render(request,'showGameByID.html', {'game': games})

def ShowDeleteGame(request, pk):
    game = Game.objects.get(pk=pk)
    return render(request,'deleteGame.html', {'game': game})

def DeleteGame(request, pk):
    if request.POST.get('delete'):
        game = Game.objects.get(pk = pk)
        game.delete()
        games = Game.objects.all()
        return render(request, 'showGame.html', {'games': games})
    elif request.POST.get('cancel'):
        games = Game.objects.all()
        return render(request, 'showGame.html', {'games': games})
    else:
        games = Game.objects.all()
        return render(request, 'showGame.html', {'games': games})

def AddGame(request):
    if request.method == "GET":
        print('add game')
        return render(request, 'addGame.html')
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        rating = request.POST.get('rating')
        price = request.POST.get('price')
        game = Game.objects.create(name=name, description=description, rating=rating, price=price)
        games = Game.objects.all()
        return render(request, 'showGame.html', {'games': games})

def EditGame(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'editGame.html', context={'game': game})
    if request.method == 'POST':
        game.name = request.POST.get('name')
        game.description = request.POST.get('description')
        game.rating = request.POST.get('rating')
        game.price = request.POST.get('price')
        game.save()
        games = Game.objects.all()
        return render(request, 'showGame.html', context={'games': games})