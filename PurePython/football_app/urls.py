from django.urls import path

from football_app.views import AddFootballView

urlpatterns = [
    path('game/', AddFootballView.as_view() ),
]