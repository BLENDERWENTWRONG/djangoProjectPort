from django import forms
from django.forms import TextInput, PasswordInput, EmailInput, FileInput, Textarea
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, UserBio

class DateInput(forms.DateInput):
    input_type = 'date'


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'phone_no', 'birthdate', 'address','avatar']

        # def __init__(self, *args, **kwargs):
        #     super(SignupForm, self).__init__(*args, **kwargs)
        #     self.fields['password1'].widget.attrs['class'] = 'form-control'
        #     self.fields['password2'].widget.attrs['class'] = 'form-control'
        #     self.fields['email'].widget.attrs['class'] = 'form-control'


class SigninForm(AuthenticationForm):
    class Meta:
        model = User
        labels = {'username': '', 'password': ''}
        fields = {'username', 'password'}


class UserBioForm(forms.ModelForm):
    class Meta:
        model = UserBio
        fields = ['bio']
        labels = {'bio': ''}
        widgets = {
            'bio': Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }