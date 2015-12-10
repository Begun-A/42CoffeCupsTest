from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('apps.hello.views',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', 'contact_data', name='contact'),
                       url(r'^requests/$', 'requests', name='requests'),
                       )

if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^uploads/(?P<path>.*)$',
                                'django.views.static.serve',
                                {'document_root': settings.MEDIA_ROOT})
                            )
