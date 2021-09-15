from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# SignUpForm extends the UserCreationForm, and is an instance of it. UCF is native to django


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
