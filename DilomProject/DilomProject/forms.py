from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms 

class CreateUserForm(UserCreationForm):
    password1=forms.CharField( widget = forms.PasswordInput(attrs={'class': 'form-control', 'aria-describedby': 'materialRegisterFormPasswordHelpBlock'}))
    password2=forms.CharField( widget = forms.PasswordInput(attrs={'class': 'form-control', 'aria-describedby': 'materialRegisterFormPasswordHelpBlock'}))
    email=forms.EmailField( widget = forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField( widget = forms.TextInput(attrs={'class': 'form-control'}))
    
    
    
    
    
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        