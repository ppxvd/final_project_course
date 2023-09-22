from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    display_name = forms.CharField(max_length=100, help_text='Required. Your displayed name.')
    username = forms.CharField(max_length=30, help_text='Required. Your username')
    password1 = forms.CharField(widget=forms.PasswordInput, help_text='Required. Enter a password.')
    password2 = forms.CharField(widget=forms.PasswordInput, help_text='Required. Enter the same password as above for verification.')
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'display_name', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))






