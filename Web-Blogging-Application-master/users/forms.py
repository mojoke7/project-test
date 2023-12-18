from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User # The model with which this form interacts with. Every form creates a new 'User'. Hence, User.
        fields = ['username', 'email', 'password1', 'password2'] # What we want to display in the form orderwise.

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User # The model with which this form interacts with. Every form creates a new 'User'. Hence, User.
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']
