from django.contrib import admin
from django.urls import path
from . import login
from Ausentismo.api.Users import *
from Ausentismo.api.permisos import *
from Ausentismo.api.historial import *
from Ausentismo.api.tiquetera import *
from Ausentismo.api.vacaciones import *
from Ausentismo.api.incapacidades import *
from Ausentismo.api.informe import *
from Ausentismo.api.notificaciones import * 
from Ausentismo.api.incapacidades import Incapacidadesdata
from Ausentismo.api.informe import Exporte_gestiones
from Ausentismo.api.data_gestiones import DataGestiones
from Ausentismo.api.graficas import DataGrafricas
from django.conf.urls.static import static
from Ausentismo.api.Users import Usersdata,usuarios
from server import settings

urlpatterns = [
    path('login/', login.login ),
    path("logout/", login.logout),
    path('register/', login.register ),
    path('Permisos/', Permisosdata.as_view()),
    path('Permisos/<int:id>', Permisosdata.as_view()),
    path('Tiquetera/',Tiqueteradata.as_view()),
    path('Tiquetera/<int:id>',Tiqueteradata.as_view()),
    path('Gestion_tiquetera/<int:id>',filtrar_campañas_tiquerera),
    path('Boss/',Usersdata.as_view()),
    path('Vacaciones/',vacacionessdata.as_view()),
    path('Vacaciones/<int:id>',vacacionessdata.as_view()),
    path("Beneficios/" , beneficios.as_view()),
    path('Beneficios/<int:id>',beneficios.as_view()),
    path("Incapacidades/", Incapacidadesdata.as_view()),
    path("Exportes/<str:tipo_permiso>/<str:fecha_inicio>/<str:fecha_fin>/<int:id>/", Exporte_gestiones.as_view()),
    path("Incapacidades_personal/", Contarincapacidades_individual),
    path("Incapacidades_campaña/<int:id>", Contarincapacidades_campaña),
    path("Gestion_permisos/", Gestion_permisos),
    path("Gestion_vacaciones/", Gestion_vacaciones),
    path("Gestion_vacaciones/<int:id>", filtrar_campañas_vacaciones),
    path("Gestion_permisos/<int:id>", filtrar_campañas),
    path("Historial_registros/<str:cedula>", HistorialData.as_view()),
    path("Historial/", HistorialMes.as_view()),
    path("data_gestiones/", DataGestiones.as_view()),
    path("data_graficas/", DataGrafricas.as_view()),
    path("Usuarios/", usuarios.as_view()),
    
] 

