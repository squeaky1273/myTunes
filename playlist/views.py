from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView

from playlist.models import Playlist, Video
from playlist.forms import PlaylistForm, VideoForm


class PlaylistListView(ListView):
    """ Renders a list of all Playlist. """
    model = Playlist

    def get(self, request):
        """ GET a list of Playlists. """
        playlists = self.get_queryset().all()
        return render(request, 'index.html', {
          'playlists': playlists
        })

class PlaylistDetailView(DetailView):
    """ Renders a specific playlist based on it's slug."""
    model = Playlist

    def get(self, request, slug):
        """ Returns a specific playlist by slug. """
        playlist = self.get_queryset().get(slug__iexact=slug)
        video_form = VideoForm()
        return render(request, 'playlist.html', {
          'playlist': playlist,
          'video_form': video_form
        })

    def post(self, request, slug):
        form = VideoForm(request.POST)
        if form.is_valid():
          video_choice = form.save(commit=False)
          video_choice.playlist_id = Playlist.objects.get(slug__iexact=slug)
          video_choice.save()
          return redirect('playlist-details-page', slug=slug)

class SignUpView(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'registration/signup.html'
  
class PlaylistCreateView(CreateView):
  template = 'new_playlist.html'
  form_class = PlaylistForm
  success_url = '/' 

  def get(self, request):
    form = PlaylistForm()
    return render(request, 'new_playlist.html', {'form': form})
  
  def post(self, request):
    if request.method == 'POST':
      form = PlaylistForm(request.POST)
      if form.is_valid():
        log = form.save()
        return HttpResponseRedirect(reverse_lazy('playlist-details-page', args=[log.slug]))
      return render(request, 'new_playlist.html', {'form': form})
