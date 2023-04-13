import re
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема', widget=forms.TextInput(attrs={'class':'form-control'}))
    content = forms.CharField(label='Текст сообщения', widget=forms.Textarea(attrs={'class':'form-control', 'rows': 5}))


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Еmail', widget=forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(label='Имя пользователя', help_text='Максимум 150 символов', widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User 
        fields = ('username', 'email', 'password1', 'password2')

  
