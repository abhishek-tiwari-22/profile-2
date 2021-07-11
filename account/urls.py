from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('profile/',views.profile,name='user profile'),
]
