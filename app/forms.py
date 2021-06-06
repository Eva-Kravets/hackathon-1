from django import forms
from .models import *


class AddApplication(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'surname', 'number', 'email', 'html', 'css', 'js', 'vue', 'react', 'ux', 'python', 'php', 'django', 'analytics', 'platform', 'students', 'web', 'mechanism', 'mobile']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя*'}),
            'surname': forms.TextInput(attrs={'placeholder': 'Фамилия*'}),
            'number': forms.TextInput(attrs={'placeholder': 'Номер телефона*'}),
            'email': forms.TextInput(attrs={'placeholder': 'Почта*'}),
        }