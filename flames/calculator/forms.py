from django import forms
from calculator.models import Data

class Flames(forms.ModelForm):
    your_name = forms.CharField(
        widget=forms.TextInput(
        attrs={
            'class': 'pure-input-rounded',
        }
    ))
    partner_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'pure-input-rounded'
        }
    ))

    class Meta:
        model = Data
        fields = ('your_name','partner_name')