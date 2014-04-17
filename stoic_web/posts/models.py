from django.db import models
from django_extensions.db.fields import CreationDateTimeField
from datetime import datetime


class Post(models.Model):
    """ A class that is parent to Blog and Event Classes
    """

    title = models.CharField(max_length=50)
    summary=models.CharField(max_length=144, blank=True)
    image = models.ImageField(upload_to="posts/%Y/%m", blank=True);
    detail=models.TextField(blank=True)
    def __unicode__(self):
        return self.title


class Event(Post):
    """ An event
    """

    location = models.CharField(max_length=50, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    
    def __unicode__(self):
        if self.start_date.date()==self.end_date.date():
            return ''.join([self.start_date.strftime('%a %d %b %Y'),' \n',self.start_date.strftime('%H:%M'),' - ',self.end_date.strftime('%H:%M')])
        else:
            return ''.join([self.start_date.strftime('%a %d %b %Y %H:%M'), ' - \n', self.end_date.strftime('%a %d %b %Y %H:%M')])

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

