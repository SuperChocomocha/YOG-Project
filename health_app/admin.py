from health_app.models import Personal_Data
from health_app.models import Health_Data
from health_app.models import Health_Info
from health_app.models import Dynamic_Info
from django.contrib import admin

admin.site.register(Personal_Data)
admin.site.register(Health_Data)
admin.site.register(Health_Info)
admin.site.register(Dynamic_Info)

