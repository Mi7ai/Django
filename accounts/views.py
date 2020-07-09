from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
# from django.views.generic import CreateView
from .forms import UserSignUpForm
# Create your views here.

class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'

class SignupView(CreateView):
    form_class = UserSignUpForm
    success_url = reverse_lazy("signupdone")
    template_name = 'accounts/signup.html'
 
class SignupDoneView(TemplateView):
   template_name = 'accounts/signup_done.html'