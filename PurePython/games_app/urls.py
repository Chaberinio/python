from django.contrib import admin
from django.urls import path, include
from games_app.views import *

urlpatterns = [
    path('show/', Show),
    path('show/<int:pk>', ShowGameByID),
    path('deleteGame/<int:pk>', DeleteGame ),
    path('showDeleteGame/<int:pk>', ShowDeleteGame),
    path('addGame/', AddGame),
    path('editGame/<int:pk>', EditGame),
    path('show/platform/<int:pk>', ShowPlatforms)


]