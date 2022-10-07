from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

def TestCookie(request):
    response = HttpResponse('Ciasteczko założone')
    response.set_cookie('test_cookie','test')
    return response

def AddCookies(request):
    if request.method == 'GET':
        return render(request, 'cookie_app/addCookie.html')
    if request.method == 'POST':
        key = request.POST.get('key')
        value = request.POST.get('value')
        response = redirect('/cookie/show/')
        response.set_cookie(key, value)
        return response

def ShowCookies(request):
    cookies = request.COOKIES
    return render(request, 'cookie_app/showCookie.html', {'cookies': cookies})

def DeleteCookies(request, key):
    response = redirect('/cookie/show')
    response.delete_cookie(key)
    return response
