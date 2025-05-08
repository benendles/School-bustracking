from django import forms
from .models import Extractedimage

class ExtractedimageForm(forms.ModelForm):
    class Meta:
        model = Extractedimage
        fields = ('image',)