from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .forms import LoginForm
from django.contrib.auth import login


def create_account(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Авторизуйте пользователя после успешной регистрации
            login(request, user)
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    return render(request, 'auth_comments_app/create_an_account.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = LoginForm()
    return render(request, 'auth_comments_app/login.html', {'form': form})





