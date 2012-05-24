'''
The admin.py file is used to configure the interface for Django
models in the built-in admin tool. At startup, Django searches for
all admin.py modules in each `INSTALLED_APPS`. All models you want
to appear in the admin tool must be registered  using the
`admin.site.register` function.

To customize the display of a model in the admin interface, sub-class
admin.ModelAdmin and provide your own values. See LandmarkAdmin example.
'''
from django.contrib import admin
from pghmarks.models import Landmark, Neighborhood


class LandmarkAdmin(admin.ModelAdmin):
    '''
    Add extra columns to the admin's list view for our
    Landmark model. Also add the ability to filter
    Landmarks by neighborhood.
    '''
    list_display = ('name', 'height', 'neighborhood',)
    list_filter = ('neighborhood',)
    
admin.site.register(Landmark, LandmarkAdmin)
admin.site.register(Neighborhood, admin.ModelAdmin)
