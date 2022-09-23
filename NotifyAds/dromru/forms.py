# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from dromru.models import AdsFilter


class UserRegForm(UserCreationForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'cli-form-field-input', 'placeholder': "Пароль"}))
    password2 = forms.CharField(label='Подтверждение Пароля', widget=forms.PasswordInput(
        attrs={'class': 'cli-form-field-input', 'placeholder': "Подтверждение пароля"}))
    # email = forms.EmailField(label='E-mail',
    #                          widget=forms.EmailInput(attrs={'class': 'cli-form-field-input', 'placeholder': "E-mail"}))
    username = forms.EmailField(label='E-mail',
                                widget=forms.EmailInput(
                                    attrs={'class': 'cli-form-field-input', 'placeholder': "E-mail"}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'cli-form-field-input', 'placeholder': "E-mail"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'cli-form-field-input', 'placeholder': "Пароль"}))


class FilterUser(forms.ModelForm):
    class Meta:
        model = AdsFilter
        fields = ['name_filter', 'url_filter', 'recheck', 'send_email', 'send_tg', 'stop_word', 'filter_word',
                  'no_price_skip']
        widgets = {
            'name_filter': forms.TextInput(attrs={'class': 'form-control'}),
            'url_filter': forms.URLInput(attrs={'class': 'form-control'}),
            'recheck': forms.Select(attrs={'class': 'form-check-label'}),
            'send_email': forms.CheckboxInput(attrs={'class': 'form-check-label'}),
            'send_tg': forms.CheckboxInput(attrs={'class': 'form-check-label'}),
            'stop_word': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Не обязательно'}),
            'filter_word': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Не обязательно'}),
            'no_price_skip': forms.CheckboxInput(attrs={'class': 'form-check-label'})
        }
