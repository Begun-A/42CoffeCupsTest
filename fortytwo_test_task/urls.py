from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login
from django.views.generic import RedirectView
from django.contrib import admin

from .settings import DEBUG, MEDIA_ROOT

admin.autodiscover()

urlpatterns = patterns('apps.hello.views',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', 'contact_data', name='contact'),
                       url(r'^requests/$', 'requests', name='requests'),
                       url(r'^edit_form/(?P<id>\d+)/$', 'edit_form_contact',
                           name='edit_form'),
                       url(r'^accounts/profile/$', RedirectView.as_view(url='/')),
                       url(r'^accounts/login/$', login, name='login')
                       )

if DEBUG:
    urlpatterns += patterns('',
                            url(r'^uploads/(?P<path>.*)$',
                                'django.views.static.serve',
                                {'document_root': MEDIA_ROOT})
                            )
