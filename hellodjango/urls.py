# coding=utf-8
from django.conf.urls import patterns, include, url
#from hellodjango.views import home,test

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

import settings
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    #url(r'^$',home),
    #url(r'^test/$',test),
    url(r'^$',include('blog.urls')),
    url(r'^tinymce/',include('tinymce.urls')),
    url(r'^comments/',include('django.contrib.comments.urls')),
    #加入css
    url(r'^site_media/(?P<path>.*)','django.views.static.serve',{'document_root': settings.STATIC_PATH}),
    #url(r'^test$',include('blog.urls')),
    # url(r'^$', 'hellodjango.views.home', name='home'),
    # url(r'^hellodjango/', include('hellodjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^e/admin/', include(admin.site.urls)),

    #url(r'^(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
)
from blog.views import archive,intro,show_post,test
urlpatterns += patterns('blog.views',
    url(r'^$',archive),
    url(r'^index$',archive),
    url(r'^intro$',intro),
    url(r'^test$',test),
    url(r'^article/(?P<pid>\d+)/', show_post ),
    url(r'^article/(?P<pid>\d+)/commentshow/$', 'show_post', name='showcomment'),
)

#urlpatterns+=patterns('',
    #(r'^site_medias/(?P<path>.*)$','django.views.static.serve',
        #{'document_root':mysite.settings.STATICFILES_DIRS, 'show_indexes': True}),
#)

