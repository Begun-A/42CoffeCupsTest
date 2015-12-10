from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

from .settings import MEDIA_ROOT

admin.autodiscover()

urlpatterns = patterns('apps.hello.views',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', 'contact_data', name='contact'),
                       url(r'^requests/$', 'requests', name='requests'),
                       )
urlpatterns += patterns('',
                        url(r'^uploads/(?P<path>.*)$',
                            'django.views.static.serve',
                            {'document_root': MEDIA_ROOT}))
urlpatterns += staticfiles_urlpatterns()
