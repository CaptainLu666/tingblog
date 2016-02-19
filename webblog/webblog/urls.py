from django.conf.urls import patterns, include, url
#from blog.views import hello,now_date,blog_list,blog_show
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('blog.views',
    # Examples:
    # url(r'^$', 'webblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^admin/doc/',include('django.contrib.admindocs.urls')),
    #url(r'^admin',include(admin.site.urls)),
    url(r'^hello','hello'),
    url(r'^time','now_date'),
    #url(r'^bloglist/$','blog.views.blog_list',name='bloglist'),
    url(r'^$','blog_list'),
    url(r'^blog/(?P<id>\d+)/$','blog_show',name='detailblog'),
)

