from django.db import models
from django_extensions.db.fields import CreationDateTimeField


class Video(models.Model):
    """Video model for youtube videos
    """
    uploaded= CreationDateTimeField()
    youtube_id=models.CharField(max_length=20)
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=200, blank=True)

 
 
