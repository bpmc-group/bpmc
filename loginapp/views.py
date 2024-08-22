# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import LoginForm

def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('dashboard')
        else:
            form.add_error(None, 'Invalid username or password')
        return redirect('dashboard')  # Simulate successful login by redirecting to dashboard
    else:
        form = LoginForm()
    return render(request, 'loginapp/login.html', {'form': form})

def dashboard(request):
    return render(request, 'dashboard/landing_page.html')
