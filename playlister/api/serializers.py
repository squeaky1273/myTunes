from rest_framework import serializers
from playlist.models import Playlist, Videos


class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
    videos = VideosSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Playlist
        fields = '__all__'