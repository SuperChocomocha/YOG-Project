from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^app/', include('health_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^start/', 'health_app.views.start'),
    url(r'^login/', 'health_app.views.login'),
    url(r'^signup/', 'health_app.views.signup'),
    url(r'^redirect/', 'health_app.views.redirect'),
)
