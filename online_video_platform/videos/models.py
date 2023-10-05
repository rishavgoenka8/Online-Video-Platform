from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Video(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_file = models.FileField(upload_to='uploads/video_files', validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mov'])])
    thumbnail = models.FileField(upload_to='uploads/thumbnails', validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])
    date_posted = models.DateTimeField(default=timezone.now)
    tags = TaggableManager()
    likes = models.ManyToManyField(User, related_name='video_likes', blank=True)
    views = models.ManyToManyField(User, related_name='video_views', blank=True)
    saved = models.ManyToManyField(User, related_name='video_saved', blank=True)
    
class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)