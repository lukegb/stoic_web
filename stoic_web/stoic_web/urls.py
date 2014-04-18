from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from website import views
from posts import views as p_views
from videos import views as v_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.flatpages import views as f_views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stoic_web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', include('website.urls')),
    url(r'^$', views.IndexView.as_view(), name='home'),
    url(r'^blog/$', p_views.BlogListView.as_view(), name='blog_index'),
    url(r'^blog/(?P<pk>[\d]+)/$', p_views.BlogDetailView.as_view(), name='blog_detail'),
    url(r'^events/$', p_views.EventListView.as_view(), name='event_index'),
    url(r'^events/(?P<pk>[\d]+)/$', p_views.EventDetailView.as_view(), name='event_detail'),
    url(r'^videos/$', v_views.VideoIndex.as_view(), name='video_index'),
    url(r'^videos/(?P<slug>[-_\w]+)/$', v_views.VideoDetailView.as_view(), name='video_detail'),
    url(r'^live/$', TemplateView.as_view(template_name="website/live.html"), name='live'),
    url(r'^tech/$', f_views.flatpage, {'url': '/tech/'},name='tech'),
    url(r'^services/$',f_views.flatpage, {'url': '/services/'}, name='services'),
    url(r'^contact/$',f_views.flatpage, {'url': '/contact/'}, name='contact'),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^admin/', include(admin.site.urls)),
) +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
