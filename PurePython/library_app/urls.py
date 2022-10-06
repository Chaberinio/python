from django.urls import path

from library_app.views import AddBookView, EditBookView, ViewBooks

urlpatterns = [
    path('library_app/add/', AddBookView.as_view()),
    path('library_app/edit/<int:pk>', EditBookView.as_view()),
    path('library_app/', ViewBooks),
]