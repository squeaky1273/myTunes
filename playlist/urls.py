from django.urls import path
from playlist.views import PlaylistListView, PlaylistCreateView, PlaylistDetailView, PlaylistUpdateView, PlaylistDeleteView


urlpatterns = [
    path('', PlaylistListView.as_view(), name='playlist-list-page'),
    # path('about/', about_page_view , name='about'),
    path('new_playlist/', PlaylistCreateView.as_view(), name='playlist-new-page'),
    path('<str:slug>/', PlaylistDetailView.as_view(), name='playlist-details-page'),
    path('<str:slug>/update', PlaylistUpdateView.as_view(), name='playlist-update-page'),
    path('<str:slug>/delete', PlaylistDeleteView.as_view(), name='playlist-delete'),
]