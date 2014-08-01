from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
import website.urls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stoic_web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', include('website.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(website.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
