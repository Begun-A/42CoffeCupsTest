from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('apps.hello.views',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', 'contact_data', name='contact'),
                       url(r'^requests/$', 'requests', name='requests'),
                       url(r'^edit_form/(?P<id>\d+)/$', 'edit_form_contact',
                           name='edit_form'),
                       )

urlpatterns += patterns('',
                        url(r'^accounts/login/$',
                            'django.contrib.auth.views.login', name='login'),
                        url(r'^accounts/profile/$',
                            RedirectView.as_view(url='/')),
                        url(r'^accounts/logout/$',
                            'django.contrib.auth.views.logout', name='logout'),
                        )

urlpatterns += patterns('',
                        url(r'^uploads/(?P<path>.*)$',
                            'django.views.static.serve',
                            {'document_root': settings.MEDIA_ROOT}))
urlpatterns += staticfiles_urlpatterns()
