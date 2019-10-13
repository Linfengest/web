from django import forms
from django.contrib.auth.models import User

class login_form(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class register_form(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2'] :
            raise forms.ValidationError('两次输入密码不相同')
        return data['password']

