from django import forms
from .models import Register
class Fo(forms.ModelForm):
    pin = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Register
        fields = ['pin','balance','first_name','middle_name','last_name','address','gender','acc_type','mail']

class PinForms(forms.Form):
    acc_num = forms.CharField(max_length=20)
    pin = forms.CharField(widget=forms.PasswordInput)