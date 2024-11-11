from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
# from .models import Client

class UserRegisterForm(UserCreationForm):
    username = forms.RegexField(regex=r"[+]375([ ]*[0-9][ ]*){9}", required=True, label="Номер телефона")
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(required=True)
    date_of_birth = forms.DateField(widget=forms.DateInput(
        attrs={
            'class':'form',
            'type':'date'
        }
    ))
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    count_of_childs = forms.IntegerField(initial=0, validators=[MinValueValidator(0), MaxValueValidator(20)])
