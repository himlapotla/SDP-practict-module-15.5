from django import forms 
from . models import Musician

class M_form(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'