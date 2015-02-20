from django.conf.urls import patterns, include, url
from django.contrib import admin

import stats.views as stats_views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', stats_views.HomeView.as_view(), name='home'),
    url(r'^ajax/stats/$', stats_views.AjaxDataView.as_view(), name='stats_data'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
