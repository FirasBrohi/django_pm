from typing import Any
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms



atters = {'class': 'form-control'}



class UserLoginForm(AuthenticationForm):
    def __init__(self,*args, **kwargs):
        super(UserLoginForm,self).__init__(*args, **kwargs)

    
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs=atters)
    )
        
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs=atters)
    )


class UserRegisterForm(UserCreationForm):
    
    
    first_name = forms.CharField(
                label='First Name',
                 widget=forms.TextInput(attrs=atters)
    )

    last_name = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(attrs=atters)
    )

    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs=atters)
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput(attrs=atters)
    )
        
    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs=atters),
    )

    password2 = forms.CharField(
        label='Password confirmation',
        strip=False,
        widget=forms.PasswordInput(attrs=atters),
    )

    class Meta(UserCreationForm.Meta):
        fields = ('first_name','last_name','username','email') 


class ProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['first_name','last_name','email']
        widgets = {
            'first_name' : forms.TextInput(attrs=atters),
            'last_name' : forms.TextInput(attrs=atters),
            'email' : forms.EmailInput(attrs=atters),
        } 