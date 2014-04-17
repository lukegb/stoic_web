from django.db import models
from django_extensions.db.fields import CreationDateTimeField
from datetime import datetime

class Category(models.Model):
    """ Base class for categories
    """

    slug=models.CharField(max_length=15, unique=True)
    name=models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

    class Meta:
        abstract=True

class Programme(Category):
    """ Which 'Programme' the video belongs to 
    """
    description=models.TextField( blank=True)
    featured=models.BooleanField( default=False)

class Genre(Category):
    """ Model for Genre, inherits Category
    """
    pass

class Video(models.Model):
    """Video model for youtube videos
    """
    uploaded= CreationDateTimeField()
    youtube_id=models.CharField(max_length=20, unique=True)
    title=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    programmes=models.ManyToManyField(Programme, blank=True)
    genre=models.ManyToManyField(Genre,blank=True)
    featured=models.BooleanField( default=False)

    def __unicode__(self):
        return self.title
    def thumbnail(self):
	    return '/'.join(['http://img.youtube.com/vi',self.youtube_id,'0.jpg'])
    def get_genres(self):
        return ', '.join( list(self.genre.all()[:2]) )
    def summary(self):
        return ''.join([self.description[:50],'...'])
    def title_summary(self):
        title_truncated=self.title[:50]
        if len(title_truncated)<len(self.title):
            return ''.join([self.title[:50],'...'])
        else:
            return self.title
    class Meta:
        ordering = ['-uploaded']
