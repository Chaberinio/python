from django.urls import path

from cart_app.views import cart

urlpatterns = [
    path('show/', cart)
]