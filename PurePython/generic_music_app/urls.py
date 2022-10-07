from django.urls import path

from generic_music_app.views import *

urlpatterns = [
    path('', SongListView.as_view()),
    path('details/<int:pk>/', SongDetailView.as_view()),
    path('add/', SongCreateView.as_view()),
    path('edit/<int:pk>', SongUpdateView.as_view()),
    path('delete/<int:pk>', SongDeleteView.as_view()),
    path('artist', ArtistListView.as_view()),
    path('detailsArtist/<int:pk>/', ArtistDetailView.as_view()),
    path('addArtist/', ArtistCreateView.as_view()),
    path('editArtist/<int:pk>/', ArtistUpdateView.as_view()),
    path('deleteArtist/<int:pk>/', ArtistDeleteView.as_view()),
]