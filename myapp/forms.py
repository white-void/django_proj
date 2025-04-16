from django import forms
from .models import *

class Dataform(forms.ModelForm):
    class Meta:
        model = metadata
        fields = ['name','auth','age','date']