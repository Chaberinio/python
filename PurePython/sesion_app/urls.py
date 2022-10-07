from django.urls import path

from sesion_app.views import counter

urlpatterns = [
    path('counter/', counter),
]