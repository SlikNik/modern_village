from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ModernUsers


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    age = forms.IntegerField()
    birthday = forms.DateField()
    address = forms.CharField(max_length=120)
    city = forms.CharField(max_length=80)
    zipcode = forms.CharField(max_length=10)
    phone = forms.BigIntegerField()
    facebook = forms.URLField()
    instagram = forms.URLField()
    twitter = forms.URLField()
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'address', 'city', 'zipcode', 'age', 'birthday']