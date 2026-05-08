from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request, 'core/home.html')


def logout_view(request):
    logout(request)

    return redirect('login')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    

    form = LoginForm(request, data=request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        
    return render(request, 'core/login.html', {
        'form': form
    })


def register_view(request):

    if request.user.is_authenticated:
        return redirect('home')
    
    form = RegisterForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        
    return render(request, 'core/register.html', {
        'form': form
    })