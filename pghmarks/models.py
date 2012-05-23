'''
Model classes for storing information on Pittsburgh landmarks.
'''
from django.db import models
from django.template.defaultfilters import slugify


class Landmark(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    height = models.PositiveIntegerField(blank=True,
                                         null=True,
                                         help_text='In feet')
    neighborhood = models.ForeignKey('Neighborhood')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Landmark, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class Neighborhood(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name
