from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.core import validators





class LoginForm(forms.Form):
    national_code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input',
        'placeholder': 'کد ملی خود را وارد نمایید',
        'pattern':"[0-9]*"
        }), max_length=10)
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-input',
        'placeholder':'رمز عبور خود را وارد نمایید'}),validators=[validators.MinLengthValidator(8)]) 
    

    def clean_national_code(self):
        national_code = self.cleaned_data.get('national_code')
        if len(national_code) < 10:
            raise ValidationError('کد ملی شما معتبر نمیباشد', code='invalid')
            
        
        return national_code



