from Ausentismo.models import Permisos, Tiquetera, Vacaciones, Incapacidades
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from Ausentismo.api.serializer import *
from django.shortcuts import get_object_or_404
from Ausentismo.api.APIs import get_data_api, get_data_api_all

class HistorialData(APIView):
    # endpoint historial
    def get(self, request, cedula):
        # datos del trabajador        
        datos = get_data_api(cedula)
        if not datos:
            return JsonResponse({"message":"La cedula digitada no existe"},status=500)
        nombre = datos.get('Nombre')
        campana = datos.get('Campaña')
        cargo = datos.get('Cargo')
        
        permisos_data = Permisos.objects.filter(cedula=cedula).values(
            'estado', 'codigo_permiso', 'fecha_inicio', 'tipo_permiso', 'parentesco'
        ).order_by('-fecha_inicio')
        tiqueteras_data = Tiquetera.objects.filter(cedula=cedula).values(
            'estado', 'codigo_tiquetera', 'fecha_peticion', 'tipo'
        ).order_by('-fecha_peticion')
        vacaciones_data = Vacaciones.objects.filter(cedula=cedula).values(
            'estado', 'Codigo_vacaciones', 'fecha_inicio', 'periodo', 'dias_vacaciones'
        ).order_by('-fecha_inicio')
        incapacidades_data = Incapacidades.objects.filter(cedula=cedula).values(
            'estado', 'radicado', 'fecha_inicio_incapacidad', 'doc_incapacidad', 'sede'
        ).order_by('-fecha_inicio_incapacidad')

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

# Historial each user
class HistorialMes(APIView):
    def get(self, request):
        data_historial = get_data_api_all(self)
        return Response(data_historial, status = 200)



