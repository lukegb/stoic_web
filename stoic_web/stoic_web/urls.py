from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from website import views
from posts import views as pviews
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stoic_web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', include('website.urls')),
    url(r'^$', views.IndexView.as_view(), name='home'),
    url(r'^blog/$', pviews.BlogListView.as_view(), name='blog_index'),
    url(r'^blog/(?P<pk>[\d]+)/$', pviews.BlogDetailView.as_view(), name='blog_detail'),
    url(r'^events/$', pviews.EventListView.as_view(), name='event_index'),
    url(r'^events/(?P<pk>[\d]+)/$', pviews.EventDetailView.as_view(), name='event_detail'),
    url(r'^videos/$', views.VideoIndex.as_view(), name='video_index'),
    url(r'^videos/(?P<slug>[-_\w]+)/$', views.VideoDetailView.as_view(), name='video_detail'),
    url(r'^live/', TemplateView.as_view(template_name="live.html"), name='live'),
    url(r'^tech/', TemplateView.as_view(template_name="tech.html"), name='tech'),
    url(r'^services/', TemplateView.as_view(template_name="services.html"), name='services'),
    url(r'^contact/', TemplateView.as_view(template_name="contact.html"), name='contact'),
    url(r'^admin/', include(admin.site.urls)),
) +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
