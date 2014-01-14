# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # User management
    url(r'^accounts/', include('allauth.urls')),

    # CMS URLs
    url(r'^', include('cms.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
