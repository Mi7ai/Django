from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import ProfileView, SignupView, SignupDoneView
from django.views.generic import base as generic_views

# app_name = 'accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('signupdone/', SignupDoneView.as_view(), name='signupdone'),
]