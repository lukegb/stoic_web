from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from website import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='home'),
    url(r'^blog/$', views.BlogListView.as_view(), name='blog_index'),
    url(r'^blog/(?P<year>\d{4})/(?P<month>(10|11|12|\d))/(?P<day>(\d|1\d|2\d|30|31))/(?P<slug>[-\w]+)/$', views.BlogArticleView.as_view(), name='blog_article'),
    url(r'^events/$', views.EventListView.as_view(), name='event_index'),
    url(r'^videos/$', views.VideoIndex.as_view(), name='video_index'),
    url(r'^videos/(?P<slug>[-_\w]+)/$', views.VideoDetailView.as_view(), name='video_detail'),
    url(r'^live/', TemplateView.as_view(template_name="live.html"), name='live'),
    url(r'^tech/', TemplateView.as_view(template_name="tech.html"), name='tech'),
    url(r'^services/', TemplateView.as_view(template_name="services.html"), name='services'),
    url(r'^contact/', TemplateView.as_view(template_name="contact.html"), name='contact'),
    url(r'^questions-live/', views.QuestionsLiveCreateView.as_view(), name='questions_live'),
)
