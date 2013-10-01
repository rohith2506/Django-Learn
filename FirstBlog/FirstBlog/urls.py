from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from blog.views import hello,current_time,hours_ahead,meta
from books import views

urlpatterns = patterns('',
	url(r'^hello/$',hello),
	url(r'^time/$',current_time),
	url(r'^another/$',current_time),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^request/$',meta),
    url(r'^search-form/$',views.search_form),
    url(r'^search/$',views.search),
    url(r'^contactus/$',views.contact),
    url(r'^contact/thanks/',views.thanks),
    # Examples:
    # url(r'^$', 'FirstBlog.views.home', name='home'),
    # url(r'^FirstBlog/', include('FirstBlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
