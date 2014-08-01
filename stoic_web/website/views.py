import random
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.list import MultipleObjectMixin
from django.views.generic.detail import SingleObjectMixin
from website.models import Blog, Event, Programme, Video

def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

class IndexView(TemplateView):
    template_name = 'index.html'

class BlogListView(ListView):
    model=Blog
    template_name = 'blog_list.html'
    context_object_name='post_list'
    paginate_by=5

class BlogArticleView(DetailView):
    model=Blog
    template_name = 'blog_article.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        kw = self.kwargs
        s = queryset.get(slug=kw['slug'])
        if str(s.date.year) != kw['year'] or \
           str(s.date.month) != kw['month'] or \
           str(s.date.day) != kw['day']:
            raise self.model.DoesNotExist('date mismatch')

        return s

class EventListView(ListView):
    model=Event
    template_name = 'event_list.html'
    context_object_name='post_list'
    paginate_by=5

class ProgrammeListView(ListView):
    model=Programme
    template_name= 'programme_list.html'


class VideoListView(ListView):
    model=Video
    template_name='video_list.html'
    paginate_by=10

class VideoGenreList(VideoListView):
    pass
class VideoIndex(ListView):
    model=Video
    template_name='video_index.html'
    paginate_by=12

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
         context = super(VideoIndex, self).get_context_data(**kwargs)
         # Add QuerySet of several featured videos
         # TODO ADD cached variable to enable dynamic changes to number of videos in admin
         featured=list( Video.objects.filter(featured=True) )
         random.shuffle(featured)
         context['object_list']=chunks(context['object_list'], 4)
         context['feat_videos'] = featured[:5]
         return context

class VideoDetailView( DetailView):
    model=Video
    template_name='video_detail.html'

    slug_field='youtube_id'


