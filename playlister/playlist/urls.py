from django.urls import path
from playlist.views import PlaylistListView, PlaylistCreateView, PlaylistDetailView


urlpatterns = [
    path('', PlaylistListView.as_view(), name='playlist-list-page'),
    path('new_playlist/', PlaylistCreateView.as_view(), name='playlist-new-page'),
    path('<str:slug>/', PlaylistDetailView.as_view(), name='playlist-details-page')
]