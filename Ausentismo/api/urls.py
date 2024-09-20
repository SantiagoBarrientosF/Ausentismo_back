from django.contrib import admin
from django.urls import path
from . import login
from Ausentismo.api.Users import *
from django.contrib.auth import logout
from  Ausentismo.api.permisos import Permisosdata
from Ausentismo.api.backend import get_datos_api

urlpatterns = [
    path('login/', login.login ),
    path("logout/", login.logout),
    path('register/', login.register ),
    path('user/', Usersdata.as_view()),
    path('permisos/', Permisosdata.as_view()),
    path("conexion/" , get_datos_api),
] 
