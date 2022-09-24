from django.contrib import admin

from vehicles import models as vehicles_models

admin.site.register(vehicles_models.Car)
