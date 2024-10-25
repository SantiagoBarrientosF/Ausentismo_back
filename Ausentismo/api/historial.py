from Ausentismo.models import Permisos, Tiquetera, Vacaciones, Incapacidades
from django.db.models import Count
from django.http import JsonResponse
from rest_framework.views import APIView
from Ausentismo.api.serializer import *
from django.shortcuts import get_object_or_404
from Ausentismo.api.APIs import get_data_api, get_data_api_Contratacion

class HistorialData(APIView):
    # endpoint historial
    def get(self, request, cedula):
        # datos del trabajador
        datos = get_data_api(cedula)
        nombre = datos.get('Nombre')
        campana = datos.get('Campaña')
        cargo = datos.get('Cargo')
        
        permisos_data = Permisos.objects.filter(cedula=cedula).values(
            'codigo_permiso', 'fecha_peticion', 'tipo_permiso', 'parentesco'
        )
        tiqueteras_data = Tiquetera.objects.filter(cedula=cedula).values(
            'codigo_tiquetera', 'fecha_peticion', 'tipo'
        )
        vacaciones_data = Vacaciones.objects.filter(cedula=cedula).values(
            'Codigo_vacacione', 'fecha_peticion', 'periodo', 'dias_vacaciones'
        )
        incapacidades_data = Incapacidades.objects.filter(cedula=cedula).values(
            'radicado', 'fecha_peticion', 'doc_incapacidad', 'sede'
        )

        # contadores
        cont_permisos = permisos_data.count()
        cont_tiqueteras = tiqueteras_data.count()
        cont_vacaciones = vacaciones_data.count()
        cont_incapacidades = incapacidades_data.count()
        
        # objetos json
        vacaciones = {
            'total': cont_vacaciones,
            'datos': list(vacaciones_data),
        }
        permisos = {
            'total': cont_permisos,
            'datos': list(permisos_data),
        }
        tiqueteras = {
            'total': cont_tiqueteras,
            'datos': list(tiqueteras_data),
        }
        incapacidades = {
            'total': cont_incapacidades,
            'datos': list(incapacidades_data),
        }
        
        historial_data = {
            'cedula': cedula,
            'nombre': nombre,
            'campana': campana,
            'cargo': cargo,
            'historial': {
                'vacaciones': vacaciones,
                'permisos': permisos,
                'tiqueteras': tiqueteras,
                'incapacidades': incapacidades,
            }
        }
        return JsonResponse(historial_data, status = 200, safe=False)
    
def get_historial_all(self):
    
    # data personas
    data_contratacion = get_data_api_Contratacion(self)
    return JsonResponse(data_contratacion, status = 200, safe = False)

