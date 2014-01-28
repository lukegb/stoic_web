from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from website import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stoic_web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', include('website.urls')),
    url(r'^$', views.IndexView.as_view(), name='home'),
    url(r'blog/$', views.BlogListView.as_view(), name='blog_index'),
    url(r'^live/', TemplateView.as_view(template_name="live.html"), name='live'),
    url(r'^admin/', include(admin.site.urls)),
)
