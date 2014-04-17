import random
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.list import MultipleObjectMixin
from django.views.generic.detail import SingleObjectMixin
from videos.models import Programme, Video

def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

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


