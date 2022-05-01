from dataclasses import field
import imp
from pyexpat import model
from django import forms
from .models import *
class userreg(forms.ModelForm):
    class Meta:
        model=Userreg
        fields="__all__"

class usertravel(forms.ModelForm):
    class Meta:
        model=Usertravel
        fields="__all__"

class bus(forms.ModelForm):
    class Meta:
        model=Bus
        fields="__all__"

    
