from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from mysite.views import hello,my_homepage_view
from books import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',my_homepage_view),
    url(r'^hello/$',hello),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search-form/$',views.search_form),
    url(r'^search/$',views.search),
)
