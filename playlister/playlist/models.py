from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Playlist(models.Model):
    playlist_name = models.CharField(max_length=200)
    video_link = models.CharField(max_length=200, blank=True, default='')
    author = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.playlist_name

    def get_absolute_url(self):
        """ Returns a fully-qualified path for a playlist (/my-new-playlist-page). """
        path_components = {'slug': self.slug}
        return reverse('playlist-details-page', kwargs=path_components)

    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a playlist is created. """
        if not self.pk:
            self.slug = slugify(self.playlist_name, allow_unicode=True)

        # Call save on the superclass.
        return super(Playlist, self).save(*args, **kwargs)

class Videos(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
