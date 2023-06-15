from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserSignupForm, UserLoginForm

def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserSignupForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                if user.user_type == 'patient':
                    return redirect('customer_dashboard')
                elif user.user_type == 'doctor':
                    return redirect('doctor_dashboard')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def customer_dashboard(request):
    return render(request, 'customer_dashboard.html')


def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html')