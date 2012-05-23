from django.contrib import admin
from pghmarks.models import Landmark, Neighborhood


admin.site.register(Landmark, admin.ModelAdmin)
admin.site.register(Neighborhood, admin.ModelAdmin)
