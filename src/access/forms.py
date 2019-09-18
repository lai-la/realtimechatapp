from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Username'
        }
        self.fields['first_name'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'First Name'
        }
        self.fields['last_name'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Last Name'
        }
        self.fields['email'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Email'
        }
        self.fields['password1'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Password'
        }
        self.fields['password2'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Confirm Password'
        }

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        
        return user