from rest_framework import serializers
from playlist.models import Playlist, Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
    video = VideoSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Playlist
        fields = '__all__'