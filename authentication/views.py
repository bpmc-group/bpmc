from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to the home page
    else:
        form = AuthenticationForm()
    return render(request, 'authentication/login.html', {'form': form})

def user_logout(request):
    logout(request)  # Logs out the current user
    return redirect('login')  # Redirect to the login page

@login_required
def home_view(request):
    return render(request, 'authentication/home.html')

def info_view(request):
    return render(request, 'authentication/info.html')

def news_view(request):
    return render(request, 'authentication/news.html')
