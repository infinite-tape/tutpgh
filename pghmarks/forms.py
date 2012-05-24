from django import forms
from pghmarks.models import Landmark


class LandmarkForm(forms.ModelForm):
    '''
    Create a custom ModelForm for the Landmark model that
    excludes the slug field for editing in the HTML form.
    '''
    class Meta:
        model = Landmark
        exclude = ('slug',)
