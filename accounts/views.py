from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User



class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home:main')
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form':form})
    

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('home:main')
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username = cd['national_code'], password = cd['password'])
            if user is not None:
                login(request, user)
                next_page = request.GET.get('next_page')
                if next_page:
                    return redirect(next_page)
                else:
                    return redirect('home:main')
            else:
                form.add_error('national_code', "کاربری با چنین اطلاعاتی وجود ندارد")
        else:
            messages.add_message(request, messages.ERROR, "اطلاعات وارد شده صحیح نمیباشد")
        return render(request, 'accounts/login.html', {'form':form})
    





class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home:main')
        form = RegisterForm()
        return render(request, 'accounts/register.html', {'form':form})
    


    def post(self, request):
        if request.user.is_authenticated:
            return redirect('home:main')
        if request.user.is_authenticated:
            return redirect('home:main')
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if User.objects.filter(national_code = cd['national_code']).exists():
                form.add_error('national_code', 'کاربری با این کد ملی وجود دارد')
            else:
                if cd['password1'] == cd['password2']:
                    user = User.objects.create_user(national_code=cd['national_code'], password=cd['password1'])
                    login(request, user)
                    return redirect('home:main')
                else:
                    form.add_error('password1', 'رمز ها با یکدیگر مطابقت ندارند')
        else:
            form.add_error('national_code', 'اطلاعات وارد شده صحیح نمیباشد')
        return render(request, 'accounts/register.html', {'form':form})





def user_logout(request):
    logout(request)
    return redirect('account:login')