from django.conf.urls import patterns, include, url
from django.contrib import admin

from launchlist.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'launchlist.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # URLs for testing
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^testTemplate/$', view_testTemplate),

    # URLs for the actual user-facing site
    url(r'^$', view_root),
    url(r'^intro/$', view_intro),
    url(r'^mission/$', view_mission),
    url(r'^spacecraft/$', view_spacecraft),
    url(r'^vehicle/$', view_launchVehicle),
    url(r'^summary/$', view_summary)
)