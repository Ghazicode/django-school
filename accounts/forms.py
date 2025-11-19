from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.core import validators



def start_with_0(value):
    if value[0]!='0':
        raise forms.ValidationError(F"شماره باید با {0} شروع بشود")



class LoginForm(forms.Form):
    national_code = forms.CharField(label='کدملی', widget=forms.TextInput(attrs={
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




class RegisterForm(forms.Form):
    national_code = forms.CharField(label='کد ملی', widget=forms.TextInput(attrs={
        'class': 'form-input',
        'placeholder': 'کد ملی خود را وارد نمایید',
        'pattern':"[0-9]*"
        }), max_length=10)
    password1 = forms.CharField(label='رمز عبور',widget=forms.PasswordInput(attrs={'class':'form-input', 'placeholder':'رمز خود را وارد نمایید'}),validators=[validators.MinLengthValidator(8)])
    password2 = forms.CharField(label='تکرار رمز عبور', widget=forms.PasswordInput(attrs={'class':'form-input', 'placeholder':'تکرار رمز خود را وارد نمایید'}), validators=[validators.MinLengthValidator(8)])



    def clean_national_code(self):
        national_code = self.cleaned_data.get('national_code')
        if len(national_code) < 10:
            raise ValidationError('تلفن وارد شده معتبر نمیباشد', code='invalid')

            
        
        return national_code
