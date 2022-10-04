from django.http import HttpResponse
from django.shortcuts import render
import random


# Create your views here.

def Hello(request):
    return HttpResponse('Hello')


def HelloName(request):
    name = request.GET.get('name', 'nieznajomy')
    return HttpResponse('Witaj,' + name)

def HelloPath(request,name):
    return HttpResponse('Witaj, ' + name)

def Add(request):
    try:
        a = float(request.GET.get('a', 0))
        b = float(request.GET.get('b', 0))
        sum = a + b
        return HttpResponse('A + B = ' + str(sum))
    except:
        return HttpResponse('Podano błędne dane!')


def Multiply(request):
    result = '<table border="1px solid black" style="border-colapse: colapse;">'
    try:
        n = int(request.GET.get('n', 0))
        for i in range(1, n + 1):
            result += '<tr>'
            for j in range(1, n + 1):
                result += '<td>' + str(i * j) + '</td>'
            result += '</tr>'
        return HttpResponse(result)
    except:
        n = 3
        for i in range(1, n + 1):
            result += '<br>'
            for j in range(1, n + 1):
                result += str(i * j) + " "
        return HttpResponse(result)


def Brothers(request):
    names = request.GET.getlist("name")
    result = '<style>p:nth-child(2n){color: red;}</style>'
    for name in names:
        result += '<p>' + name + '</p>'

    return HttpResponse(result)


def Fibbo(request):
    result = "<ul>"
    a = 1
    b = 0
    c = 0
    try:
        n = int(request.GET.get("n", 0))
        result += '<li> 1 </li>'
        for i in range(1, n):
            result += '<li>' + str(b + a) + '</li>'
            c = b
            b = a
            a = c + a
        return HttpResponse(result)
    except ValueError:
        return HttpResponse('Podano błędne dane!')


number = random.randint(1, 100)


def Game(request):
    global number
    try:
        messege = ""
        guess = int(request.GET.get("guess"))

        if guess == number:
            messege = "Zgadłeś!"
            number = random.randint(1, 100)
        elif guess < number:
            messege = "Twoja liczba jest za mała!"
        elif guess > number:
            messege = "Twoja liczba jest za duża!"
        return HttpResponse('<form><input name="guess" placeholder="podaj liczbę(1-100)"></form>' + messege)
    except:
        number = random.randint(1, 100)
        return HttpResponse('<form><input name="guess" placeholder="podaj liczbę(1-100)"></form>' + messege)

def Article(request, id):
    if id == 0 or id > 3:
        return HttpResponse('Brak artykułu dla podanego id!')
    elif id == 1:
        return HttpResponse('Artykuł 1')
    elif id == 2:
        return HttpResponse('Artykuł 2')
    elif id == 3:
        return HttpResponse('Artykuł 3')

def Greetings(request, name, num):
    result = ''
    for i in range(0, num):
        result += 'Hello, ' + name + '<br>'
    return HttpResponse(result)

def Calc(request,numA, operation, numB):

    try:
        NumA = float(numA)
        NumB = float(numB)
        if operation == 'plus':
            return HttpResponse('A + B = ' + str(NumA + NumB))
        elif operation == 'minus':
            return HttpResponse('A - B = ' + str(NumA - NumB))
        elif operation == 'divide':
            if NumA == 0 or NumB == 0:
                return HttpResponse('Nie można dzielić przez 0!')
            else:
                return HttpResponse('A / B = ' + str(NumA / NumB))
        elif operation == 'multiply':
            return HttpResponse('A * B = ' + str(NumA * NumB))
        else:
            return HttpResponse('Nie można wykonać tej operacji!')
    except:
        return HttpResponse('Nieprawidłowe dane!')

def RandomGenerator(request, min, max,throws=1):
    sum = 0
    for i in range(0, throws):
        num = random.randint(min, max)
        sum += num

    return HttpResponse(sum)

def Index(request):
    return render(request, 'first_app/index.html', context={
                                            'messege':'Wiadomość z szablonu',
                                            'names' : ['Jan','Ewa','Adam','Maciej']})

def Form(request):
    if request.method == "GET":
        return render(request, 'first_app/form.html')
    if request.method == "POST":
        return  HttpResponse(request.POST.get('test', 'brak parametru'))

def FizzBuzz(request, n = 1):
    data = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            data.append('FizzBuzz')
        elif i % 5 == 0:
            data.append('Buzz')
        elif i % 3 == 0:
            data.append('Fizz')
        else:
            data.append(i)
    return render(request, 'first_app/fizz_buzz.html', context={'data': data})

def MultiplyTemplate(request, n = 5):
    return render(request, 'first_app/multiply.html', context={'elements' : range(1, n+1)})

def RpgGame(request):
    PlayerName = 'Gracz'
    EnemyName = 'Wróg'
    PlayerWeapon = 'Miecz'
    EnemyWeapon = 'Topór'
    PlayerHp = random.randint(100, 200)
    PlayerAtk = random.randint(1, 100)
    PlayerDef = random.randint(1, 20)
    EnemyHp = random.randint(100, 500)
    EnemyAtk = random.randint(10, 20)
    EnemyDef = random.randint(1, 20)
    result = ''
    turn = 1
    GameResult = []
    PlayerCurrentHp = PlayerHp
    EnemyCurrentHp = EnemyHp
    while PlayerCurrentHp > 0 and EnemyCurrentHp > 0:
        result = ''
        result += 'Turn' + str(turn) + ' '
        PlayerDMG = random.randint(1, 100) + PlayerAtk
        result += 'Player damage: ' + str(PlayerDMG) + ' '
        EnemyDMG = random.randint(10, 20) + EnemyAtk
        result += 'Enemy damage: ' + str(EnemyDMG) + ' '
        PlayerCurrentHp = PlayerCurrentHp - (EnemyDMG - PlayerDef)
        result += 'Player health points: ' + str(PlayerCurrentHp) + ' '
        EnemyCurrentHp = EnemyCurrentHp - (PlayerDMG - EnemyDef)
        result += 'Enemy health points: ' + str(EnemyCurrentHp) + ' '
        GameResult.append(result)
        if PlayerCurrentHp < 0:
            result = ''
            result += 'GAME OVER - you lose'
            GameResult.append(result)
        elif EnemyCurrentHp < 0:
            result = ''
            result += 'NEXT LEVEL - you win'
            GameResult.append(result)
        turn += 1

    return render(request, 'first_app/rpg_game.html', context={'EnemyAtk' : EnemyAtk,
                                                                'EnemyHp' : EnemyHp,
                                                                'PlayerAtk' : PlayerAtk,
                                                                'PlayerHp': PlayerHp,
                                                                'EnemyName' : EnemyName,
                                                                'EnemyWeapon': EnemyWeapon,
                                                                'PlayerName' : PlayerName,
                                                                'PlayerWeapon' : PlayerWeapon,
                                                                'PlayerDef' : PlayerDef,
                                                                'EnemyDef' : EnemyDef,
                                                                'GameResult' : GameResult})