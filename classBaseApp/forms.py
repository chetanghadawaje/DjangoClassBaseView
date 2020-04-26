from django import forms
from .models import *


class Frm_Customer(forms.ModelForm):
    cust_name = forms.CharField(required=True, max_length=50, widget=forms.TextInput())
    site_name = forms.CharField(required=False, max_length=50, widget=forms.TextInput())
    phone_no = forms.CharField(required=False, max_length=50, widget=forms.TextInput())

    class Meta:
        model = customerModal
        fields = '__all__'
