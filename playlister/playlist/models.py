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

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a playlist is created. """
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)

        # Call save on the superclass.
        return super(Playlist, self).save(*args, **kwargs)

class Videos(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
