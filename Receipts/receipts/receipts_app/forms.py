from django import forms
from .models import Receipt
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ReceiptForm(forms.ModelForm):

    class Meta:
        model = Receipt
        fields = ['title', 'description', 'author']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
