from django.contrib import admin
from django.urls import path
from . import login

from django.contrib.auth import logout


urlpatterns = [
    path('login/', login.login ),
    path("logout/", login.logout),
    path('register/', login.register ),
] 
