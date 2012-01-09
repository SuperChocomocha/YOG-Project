from django.conf.urls.defaults import *
from health_app.models import Personal_Data, Health_Data, Health_Info, Dynamic_Info

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('health_app.views',
    url(r'^(?P<acc_id>\d+)/homepage/', 'homepage'),
    url(r'^(?P<acc_id>\d+)/input_hr/', 'input_hr'),
    url(r'^(?P<acc_id>\d+)/details/', 'details'),
)

