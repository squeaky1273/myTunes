from django import forms
from playlist.models import Playlist, Video

class PlaylistForm(forms.ModelForm):
    """ Render and process a form based on the Playlist model. """
    class Meta:
        model = Playlist
        fields = '__all__'

class VideoForm(forms.ModelForm):
    """ Render and process a form based on the Video model. """
    class Meta:
        model = Video
        fields = ['video']
