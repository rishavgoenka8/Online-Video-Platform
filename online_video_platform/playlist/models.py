from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from videos.models import Video
from django.core.validators import FileExtensionValidator

# Create your models here.
class Playlist(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    videos = models.ManyToManyField(Video, related_name='playlist_videos', blank=True)
    thumbnail = models.FileField(upload_to='playlists/thumbnails', validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])
    date_posted = models.DateTimeField(default=timezone.now)
