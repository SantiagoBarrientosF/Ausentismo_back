from django.contrib import admin
from django.urls import path
from . import login
from Ausentismo.api.Users import *
from django.contrib.auth import logout
from  Ausentismo.api.permisos import Permisosdata
from Ausentismo.api.backend import get_datos_api
from Ausentismo.api.tiquetera import *

urlpatterns = [
    path('login/', login.login ),
    path("logout/", login.logout),
    path('register/', login.register ),
    path('permisos/', Permisosdata.as_view()),
    path('tiquetera/',Tiqueteradata.as_view()),
    path("conexion/<str:cedula>" , get_datos_api),
] 
