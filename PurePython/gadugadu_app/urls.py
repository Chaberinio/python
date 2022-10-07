from django.contrib import admin
from django.urls import path
from firstapp.views import *
from gadugadu_app.views import ShowMessage, ShowFormView

urlpatterns = [
    path('message/', ShowMessage ),
    path('form/', ShowFormView.as_view()),
]