from django.conf.urls.defaults import patterns, include, url



urlpatterns = patterns('labo.login.views',


    url(r'^login/', 'login', name='login'),
    url(r'^logout/', 'logout', name='logout'),


)
