from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import view

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HelloWorld.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),


    #url(r'^$', view.hello),
    url(r'^hello$', view.hello),

)
