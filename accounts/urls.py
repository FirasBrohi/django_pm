from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path,include
from . import forms
from accounts.views import RegisterView,edit_profile


urlpatterns = [
    path("login/", LoginView.as_view(authentication_form=forms.UserLoginForm), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/',RegisterView.as_view(),name ='register' ),
    path('profile/',edit_profile, name ='profile' ),
    path('',include('django.contrib.auth.urls')),

]