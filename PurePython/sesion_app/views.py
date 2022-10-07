from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def counter(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    return HttpResponse(str(request.session.get('counter')))