from django.contrib import admin
from django.urls import path
from . import login
from Ausentismo.api.Users import *
from django.contrib.auth import logout
from  Ausentismo.api.permisos import Permisosdata
# from Ausentismo.api.backend import get_datos_api
from Ausentismo.api.tiquetera import *
from Ausentismo.api.vacaciones import *
from Ausentismo.api.backend import get_datos_api
urlpatterns = [
    path('login/', login.login ),
    path("logout/", login.logout),
    path('register/', login.register ),
    path('Permisos/', Permisosdata.as_view()),
    path('Tiquetera/',Tiqueteradata.as_view()),
    path('Boss/',Usersdata.as_view()),
    path('Vacaciones/',vacacionessdata.as_view()),
    path("conexion/<str:cedula>" , get_datos_api),
] 
