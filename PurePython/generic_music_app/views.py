from django.shortcuts import render
from django.views.generic import *

from generic_music_app.models import Song, Artist


# Create your views here.

class SongListView(ListView):
    model = Song
    template_name = 'generic_music_app/list.html'

class SongDetailView(DetailView):
    model = Song
    template_name = 'generic_music_app/detail.html'

class SongCreateView(CreateView):
    model = Song
    fields = '__all__'
    template_name = 'generic_music_app/form.html'
    success_url = '/music/'

class SongUpdateView(UpdateView):
    model = Song
    fields = '__all__'
    template_name = 'generic_music_app/form.html'
    success_url = '/music/'

class SongDeleteView(DeleteView):
    model = Song
    template_name = 'generic_music_app/delete.html'
    success_url = '/music/'

class ArtistListView(ListView):
    model = Artist
    template_name = 'generic_music_app/listArtist.html'

class ArtistDetailView(DetailView):
    model = Artist
    template_name = 'generic_music_app/detail.html'

class ArtistCreateView(CreateView):
    model = Artist
    fields = '__all__'
    template_name = 'generic_music_app/form.html'
    success_url = '/music/artist'

class ArtistUpdateView(UpdateView):
    model = Artist
    fields = '__all__'
    template_name = 'generic_music_app/form.html'
    success_url = '/music/'

class ArtistDeleteView(DeleteView):
    model = Artist
    template_name = 'generic_music_app/delete.html'
    success_url = '/music/'