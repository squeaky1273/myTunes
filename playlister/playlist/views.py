from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Videos, Playlist

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'playlist/index.html'

    def get_queryset(self):
        """
        Return the last five published playlists (not including those set to be
        published in the future).
        """
        return Playlist.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    pass

class ResultsView(generic.DetailView):
    model = Playlist
    template_name = 'playlist/results.html'
