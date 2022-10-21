from typing import Dict, Any

from django import forms
from django.forms import Form, ModelForm
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm as BasePasswordChangeForm

from core.mixins import AddClassNameMixin, AddAttributeMixin

User = get_user_model()


class UserUpdateForm(AddClassNameMixin, AddAttributeMixin, ModelForm):

    custom_attributes = {
        'avatar': {
            'onchange': 'document.getElementById("userAvatar").src = window.URL.createObjectURL(this.files[0])',
        }
    }

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'avatar',
            'account_type'
        ]


class LoginForm(AddClassNameMixin, Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    remember_me = forms.BooleanField(widget=forms.CheckboxInput(attrs={'id':'flexCheckDefault'}), required=False)

class RegisterForm(AddClassNameMixin, forms.Form):
    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    email = forms.EmailField(widget=forms.EmailInput())
    username = forms.CharField(widget=forms.TextInput())
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'id':'password1'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'id':'password2'}))

    def clean(self) -> Dict:
        cleaned_data = super().clean()

        if cleaned_data['password1'] != cleaned_data['password2']:
            raise ValidationError('Passwords do not match!')

        return cleaned_data

    def clean_email(self) -> Any:
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise ValidationError('This email is already taken!')

        return email


class PasswordChangeForm(AddClassNameMixin,BasePasswordChangeForm):
    pass
