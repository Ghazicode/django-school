from django.shortcuts import render, redirect
from .forms import LoginForm
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from time import sleep

# def register(request):
#     form = LoginForm()
#     return render(request, 'accounts/register.html', {'form':form})



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
                
                return redirect('home:main')
            else:
                messages.add_message(request, messages.ERROR, "کاربری با چنین اطلاعاتی وجود ندارد")
        else:
            messages.add_message(request, messages.ERROR, "اطلاعات وارد شده صحیح نمیباشد")
        return render(request, 'accounts/login.html', {'form':form})
    







def register(request):
    return render(request, 'accounts/register.html')

def user_logout(request):
    logout(request)
    return redirect('account:login')