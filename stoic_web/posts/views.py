from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.list import MultipleObjectMixin
from django.views.generic.detail import SingleObjectMixin
from posts.models import Blog, Event

class BlogListView(ListView):
    model=Blog
    template_name = 'blog_list.html'
    context_object_name='post_list'
    paginate_by=5

class BlogDetailView(DetailView):
    model=Blog
    template_name='blog_detail.html'
    context_object_name='post'

class EventListView(ListView):
    model=Event
    template_name = 'event_list.html'
    context_object_name='post_list'
    paginate_by=5

class EventDetailView(DetailView):
    model=Event
    template_name='event_detail.html'
    context_object_name='post'
