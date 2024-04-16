from django.shortcuts import render

# Create your views here.
def login(request):
    context = {
        'title': 'Авторизация',
    }
    return render(request, 'users/login.html', context)

def register(request):
    context = {
        'title': 'Регистрация',
    }
    return render(request, 'users/register.html', context)

def profile(request):
    context = {
        'title': 'Профиль',
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    ...