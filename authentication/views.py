from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import CustomAuthenticationForm

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            remember_me = form.cleaned_data.get('remember_me')
            request.session.set_expiry(0 if remember_me else None)  # Session expiry
            return redirect('dashboard')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'authentication/login.html', {'form': form})

@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')
