from django.db import models
from django_extensions.db.fields import CreationDateTimeField

class Programme(models.Model):
    """ Which 'Programme' the video belongs to 
    """
    slug=models.CharField(max_length=15, unique=True)
    name=models.CharField(max_length=50)
    description=models.TextField( blank=True)
    featured=models.BooleanField( default=False)
    def __unicode__(self):
        return self.name

class Video(models.Model):
    """Video model for youtube videos
    """
    uploaded= CreationDateTimeField()
    youtube_id=models.CharField(max_length=20, unique=True)
    title=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    programmes=models.ManyToManyField(Programme)

    def __unicode__(self):
        return self.title

    def thumbnail(self):
	    return '/'.join(['http://img.youtube.com/vi',self.youtube_id,'0.jpg'])
