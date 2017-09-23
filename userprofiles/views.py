from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView

from .models import Profile
from .forms import SignUpForm


# Create your views here.

class SignUp(CreateView):
    model = Profile
    field = ['first_name', 'last_name', 'email']
    template_name = 'registration.html'
    form_class = SignUpForm

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect('Movie:list')

class SignIn(LoginView):
    template_name = 'login.html'

class SignOut(LogoutView):
    pass
