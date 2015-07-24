from django.conf.urls import patterns, url
from polls.views import index

urlpatterns = patterns('',
    url(r'^$', index, name="index"),
	)