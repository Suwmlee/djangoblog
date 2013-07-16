from django.conf.urls import patterns, url

from blog.views import archive,intro,show_post

urlpatterns = patterns('',
    url(r'^$',archive),
    url(r'^index$',archive),
    url(r'^intro$',intro),
	url(r'^article/(?P<pid>\d+)/', show_post),
)
