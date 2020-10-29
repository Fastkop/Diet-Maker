from django import forms
from django.contrib.auth.models import User
from core.models import Profile
from django.contrib.auth.forms import UserCreationForm
import datetime


class SignUp(UserCreationForm):
    email = forms.EmailField(max_length=200, widget=forms.TextInput(
        attrs={'placeholder': 'Email'}
    ))
    username = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={'placeholder': 'Username'}
    ))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'First Name'}
    ))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Last Name'}
    ))
    password1 = forms.Field(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}
    ))
    password2 = forms.Field(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}
    ))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class UpdateProfile(forms.ModelForm):
    age = forms.IntegerField(min_value=0, max_value=100,
                             widget=forms.NumberInput(attrs={
                                 'placeholder': 'Age'
                             })
                             )
    weight = forms.FloatField(min_value=30, max_value=500, widget=forms.NumberInput(
        attrs={'placeholder': 'Weight'}
    ))
    height = forms.FloatField(min_value=30, max_value=300, widget=forms.NumberInput(
        attrs={'placeholder': 'Height'}
    ))
    photo = forms.ImageField(label="Choose profile photo", widget=forms.FileInput(
        attrs={'placeholder': 'Photo'}
    ))
    gender = forms.CharField(max_length=1, widget=forms.Select(choices=Profile.GENDER_CHOICES))

    class Meta:
        model = Profile
        exclude = ['user', 'bmi', 'diet']


class Login(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]
