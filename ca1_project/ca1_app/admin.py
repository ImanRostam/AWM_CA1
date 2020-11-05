from django.contrib.gis import admin
from .models import WorldBorder

# register your models here

admin.site.register(WorldBorder, admin.GeoModelAdmin)