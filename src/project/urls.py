from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'scouter.views.index', name='index'),
    url(r'^contact$', 'scouter.views.contact', name='contact'),
    url(r'^games$', 'scouter.views.games', name='games'),
)
