"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""
from datetime import date
from django.test import TestCase
from django.template.defaultfilters import slugify
from pghmarks.models import Landmark, Neighborhood


class LandmarkTest(TestCase):
    def test_slug_generation(self):
        """
        Tests that slugs auto-generate on save().
        """
        oakland = Neighborhood(name='Oakland')
        oakland.save()
        cathedral = Landmark(name='Cathedral of Learning',
                             opened_date=date(year=1936, month=1, day=1),
                             height=535,
                             neighborhood=oakland)
        cathedral.save()
        # test that slug was generated from the name field
        self.assertEquals(cathedral.slug, slugify(cathedral.name))
