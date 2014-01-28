from django.db import models
from django_extensions.db.fields import CreationDateTimeField
from datetime import datetime
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
    title=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    programmes=models.ManyToManyField(Programme)

    def __unicode__(self):
        return self.title

    def thumbnail(self):
	    return '/'.join(['http://img.youtube.com/vi',self.youtube_id,'0.jpg'])
    
    def summary(self):
        return self.description[:144]

    class Meta:
        ordering = ['-uploaded']

class Post(models.Model):
    """ A class that is parent to Blog and Event Classes
    """

    title = models.CharField(max_length=50)
    summary=models.CharField(max_length=144, blank=True)
    image = models.ImageField(upload_to="posts/%Y/%m", blank=True);
    detail=models.TextField(blank=True)


class Event(Post):
    """ An event
    """

    location = models.CharField(max_length=50, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    class Meta:
        ordering = ['-start_date']
class Blog(Post):
    """ A Blog Post
    """

    date = models.DateTimeField(default=datetime.now())
    author = models.CharField(max_length=40,blank=True, default='STOIC')
    class Meta:
        ordering = ['-date']

class Link(models.Model):
    """ Links for post models
    """
    WEBSITE='WW'
    YOUTUBE='YT'
    FACEBOOK='FB'
    TWITTER='TW'
    OTHER='OT'
    KIND_CHOICES= (
        (WEBSITE, 'Website'),
	(YOUTUBE, 'Youtube'),
	(FACEBOOK, 'Facebook'),
	(TWITTER, 'Twitter'),
	(OTHER, 'Other'),
    )
    description=models.CharField(max_length=40)
    url=models.URLField()
    kind=models.CharField(max_length=2, choices=KIND_CHOICES, default=WEBSITE)
    post=models.ForeignKey(Post, related_name="post")

