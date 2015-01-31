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
	    return '/'.join(['http://img.youtube.com/vi',self.youtube_id,'maxresdefault.jpg'])
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
        get_latest_by = 'uploaded'

class Post(models.Model):
    """ A class that is parent to Blog and Event Classes
    """

    slug = models.SlugField(blank=False, null=False)
    title = models.CharField(max_length=50)
    summary = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to="posts/%Y/%m", blank=True);
    detail = models.TextField(blank=True, null=False)
    def __unicode__(self):
        return self.title


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
    author = models.CharField(max_length=40,blank=True, default='ICTV')
    class Meta:
        ordering = ['-date']
        get_latest_by = 'date'

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

class QuestionsLive(models.Model):
    """ Form for IQL
    """
    email = models.EmailField()
    name = models.CharField(max_length=100)
    question = models.TextField()