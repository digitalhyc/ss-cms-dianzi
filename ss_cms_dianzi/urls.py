from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


from article.views import show_article


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ss_cms_dianzi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^article/$', show_article),

)
