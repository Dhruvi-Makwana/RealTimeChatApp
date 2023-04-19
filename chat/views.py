from django.shortcuts import render
from django.contrib.auth.views import (
    LoginView,LogoutView
)
from .forms import LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView


class Index(LoginRequiredMixin, TemplateView):
    template_name = "chat/index.html"


class AdminLogin(LoginView):
    template_name = 'chat/login.html'
    authentication_form = LoginForm


class Adminlogout(LoginRequiredMixin, LogoutView):
    pass