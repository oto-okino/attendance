from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# from .models import User
from .forms import SignupForm, LoginForm

# Create your views here.
def landing_view(request):
    return render(request, 'accounts/landing.html')

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("landing")

    else:
        form = SignupForm()

    return render(request, "accounts/signup.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid(): # form は入力検証のみで login() まではやらないので 後で login する必要がある
            user = form.get_user() # form から user を取得する
            login(request, user)
            return redirect("dashboard")

    else:
        form = LoginForm()

    return render(request, "accounts/login.html", {"form": form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('landing')