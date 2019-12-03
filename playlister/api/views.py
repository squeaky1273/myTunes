from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from playlist.models import Playlist, Videos
from .serializers import PlaylistSerializer
# Create your views here.
class PlaylistList(APIView):
    def get(self, request):
        playlists = Playlist.objects.all()[:20]
        data = PlaylistSerializer(playlists,many=True).data
        return Response(data)

class PlaylistDetail(APIView):
    def get(self, request, pk):
        playlist = get_object_or_404(Playlist, pk=pk)
        data = PlaylistSerializer(playlist).data
        return Response(data)