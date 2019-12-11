from django.test import TestCase
from django.contrib.auth.models import User

from playlist.models import Playlist

# Create your tests here.
class PlaylistTestCase(TestCase):
    def test_is_true(self):
        """ Tests if True is equal to True. Should always pass. """
        self.assertEqual(True, True)

    def test_playlist_slugify_on_save(self):
        """ Tests the slug generated when saving a Playlist. """
        # Author is a required field in our model.
        # Create a user for this test and save it to the test database.
        user = User()
        user.save()

        # Create and save a new page to the test database.
        playlist = Playlist(title="My Test Playlist", description="test", author=user)
        playlist.save()

        # Make sure the slug that was generated in Playlist.save()
        # matches what we think it should be.
        self.assertEqual(playlist.slug, "my-test-playlist")