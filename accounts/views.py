from django.shortcuts import render
from django.views import View
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.http import HttpResponseRedirect
from .models import *


User = get_user_model()


class RegistrationView(View):

    template_name = 'accounts/registration.html'

    def get(self, request, *args, **kwargs):

        form = RegistrationForm(request.POST or None)
        context = {
            'form': form
        }
        return render(self.request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            new_user.set_password(password)
            password_check = form.cleaned_data['password_check']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            new_user.save()
            UserAccount.objects.create(user=User.objects.get(username=new_user.username),
                                       first_name=new_user.first_name,
                                       last_name=new_user.last_name,
                                       email=new_user.email)
            return HttpResponseRedirect('/')
        context = {
            'form': form
        }
        return render(self.request, self.template_name, context)


class LoginView(View):

    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):

        form = LoginForm(request.POST or None)
        context = {
            'form': form
        }
        return render(self.request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(self.request, user)
            return HttpResponseRedirect('/')
        context = {
            'form': form
        }
        return render(self.request, self.template_name, context)
