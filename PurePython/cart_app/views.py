from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def cart(request):
    if request.method == 'GET':
        return render(request, 'cart_app/cart.html')
    if request.method == 'POST':
        cart = request.POST.getlist('cart')
        if 'cart' in request.session:
            request.session['cart'] = cart
            return HttpResponse(' '.join(request.session.get('cart')))
        else:
            cart = request.POST.getlist('cart')
            request.session['cart'] = cart
            return HttpResponse(' '.join(request.session.get('cart')))
