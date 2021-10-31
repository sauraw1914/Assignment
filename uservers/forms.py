from django import forms
from django.forms import Form,ModelForm,ModelChoiceField,CharField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from uservers.models import *


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=255, help_text="Must Enter Valid E-mail!")
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',
                  'username', 'password1', 'password2')



class LoginForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "password")

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            
            if not authenticate(username=username, password=password):
                raise forms.ValidationError("invalid Login")


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["text"]
        # exclude = ["user"]