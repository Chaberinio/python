from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.views import View

from library_app.forms import BookForm
from library_app.models import Book


# Create your views here.
class AddBookView(View):
    def get(self, request):
        form = BookForm()
        return render(request, 'library_app/book_form.html', {'form': form, 'message' : 'Dodaj książkę'})

    def post(self, request):
        form = BookForm(request.POST, instance=Book())
        if form.is_valid():
            form.save()
            return redirect('/library_app/')
        else:
            return render(request, 'library_app/book_form.html', {'form': form, 'message' : 'Dodaj książkę'})

class EditBookView(View):
    def get(self, request, pk):
        form = BookForm(instance=Book.objects.get(pk=pk))
        return render(request, 'library_app/edit_book.html', {'form': form, 'message' : 'Edytuj książkę'})

    def post(self, request, pk):
        form = BookForm(request.POST, instance=Book.objects.get(pk=pk))
        if form.is_valid():
            form.save()
            return redirect('/library_app/')
        else:
            return render(request, 'library_app/edit_book.html', {'form': form, 'message' : 'Edytuj książkę'})


def ViewBooks(request):
    books = Book.objects.all()
    return render(request, 'library_app/view_books.html', {'books': books})
