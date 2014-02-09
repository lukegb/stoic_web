from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from website.models import Blog, Event, Programme

class IndexView(TemplateView):
	template_name = 'index.html'

class BlogListView(ListView):
    model=Blog
    template_name = 'blog_list.html'
    context_object_name='post_list'
    paginate_by=5

class EventListView(ListView):
    model=Event
    template_name = 'event_list.html'
    context_object_name='post_list'
    paginate_by=5
