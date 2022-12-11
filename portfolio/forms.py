from django import forms
from django.forms import TextInput, PasswordInput, EmailInput, FileInput, Textarea
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import portfolio



class createportfolio(forms.ModelForm):
    class Meta:
        model = portfolio
        fields = ['creator','bio','workField','careersum']
        labels = {'bio': '',
                  'workField':'',
                  'careersum': 'Career Summary',}
