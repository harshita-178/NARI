from django import forms
from .models import Nari

class Contact(forms.ModelForm):
    class Meta:
        model=Nari
        fields= ['email','password']
