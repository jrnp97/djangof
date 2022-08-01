from django import forms

from .models import Deudor


class GoogleForm(forms.Form):
    input = forms.CharField(max_length=50)


class DeudorForm(forms.ModelForm):
    class Meta:
        model = Deudor
        fields = '__all__'
