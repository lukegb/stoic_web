import random
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.views.generic.list import MultipleObjectMixin
from django.views.generic.detail import SingleObjectMixin
from django.utils import timezone

from vanilla import CreateView

from website.models import Blog, Event, Programme, Video, QuestionsLive
from website.forms import QLForm

def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        kwargs = super(IndexView, self).get_context_data(**kwargs)

        kwargs['latest_blog'] = Blog.objects.count() and Blog.objects.latest()

        kwargs['latest_show'] = Video.objects.count() and Video.objects.latest()

        evs = Event.objects.filter(start_date__gt=timezone.now()).order_by('start_date')
        if evs:
            kwargs['next_event'] = evs[0]

        kwargs['live_streaming'] = False

        return kwargs

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
         #featured=list( Video.objects.filter(featured=True) )
         #random.shuffle(featured)
         #context['feat_videos'] = featured[:5]
         return context

class VideoDetailView( DetailView):
    model=Video
    template_name='video_detail.html'

    slug_field='youtube_id'


# class QuestionsLiveCreateView(CreateView):
#     model = QuestionsLive
#     template_name = 'questions_live.html'
#     form_class = QLForm

class QuestionsLiveCreateView(CreateView):

    model = QuestionsLive
    template_name = 'questions_live.html'
    form_class = QLForm

    # def get_form_kwargs(self):
    #     kwargs = super(QuestionsLiveCreateView, self).get_form_kwargs()
    #     kwargs['ip'] = self.request.META['HTTP_X_FORWARDED_FOR']
    #     kwargs['user_agent'] = self.request.META['HTTP_USER_AGENT']
    #     # print kwargs
    #     return kwargs

    def get_form(self, data=None, files=None, **kwargs):
        if data:
            data_cp = data.copy()
        else:
            data_cp = {}

        data_cp['ip'] = self.request.META['REMOTE_ADDR']
        data_cp['user_agent'] = self.request.META['HTTP_USER_AGENT']

        return QLForm(data_cp, files, **kwargs)

    def form_valid(self, form):
        form.save()
        return render(self.request, self.template_name,  {'complete': True})
