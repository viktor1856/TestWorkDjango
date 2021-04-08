from django import forms


class AvtorizeForm(forms.Form):
    username = forms.CharField(label='Логин', max_length=40,error_messages={'required': 'Пожалуйста введите свой логин'},empty_value='Логин')
    password = forms.CharField(label='Пароль',max_length=40, widget=forms.PasswordInput)


class userRegistration(forms.Form):
    username = forms.CharField(label='Логин', max_length=40,error_messages={'required': 'Пожалуйста введите свой логин'},empty_value='Логин')
    password = forms.CharField(label='Пароль',max_length=40, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль',max_length=40, widget=forms.PasswordInput)