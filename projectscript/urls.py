# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'application.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^function/$', 'application.views.function_for_ajax'),
    url(r'^admin/', include(admin.site.urls)),
)
