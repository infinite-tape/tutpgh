from django import forms
from pghmarks.models import Landmark


class LandmarkForm(forms.ModelForm):
    class Meta:
        model = Landmark
        exclude = ('slug',)
        
    
