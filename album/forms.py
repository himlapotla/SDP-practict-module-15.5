from django import forms 
from . models import Album


class A_form(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
