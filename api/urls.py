from django.urls import path
from .views import  PlaylistList, PlaylistDetail

urlpatterns = [
    path('playlists/', PlaylistList.as_view(), name='playlists_list'),
    path('playlists/<int:pk>/', PlaylistDetail.as_view(), name='playlists_detail')
]