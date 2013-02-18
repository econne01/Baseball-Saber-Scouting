from django.conf.urls import patterns, include, url
from scouter.views import BatterDetail

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'scouter.views.index', name='index'),
    url(r'^contact$', 'scouter.views.contact', name='contact'),
    url(r'^games$', 'scouter.views.games', name='games'),
    url(r'^batter/(?P<pk>\d+)$', BatterDetail.as_view(template_name='batter_detail.html'), name='games'),
)
