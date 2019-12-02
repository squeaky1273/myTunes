import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Playlists(models.Model):
    playlist_name = models.CharField(max_length=200)
    video_link = models.CharField(max_length=200, blank=True, default='')
    author = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.playlist_name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Videos(models.Model):
    playlist = models.ForeignKey(Playlists, on_delete=models.CASCADE)
