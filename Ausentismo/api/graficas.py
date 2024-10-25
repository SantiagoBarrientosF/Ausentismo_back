from Ausentismo.models import Permisos, Tiquetera, Vacaciones, Incapacidades
from django.db.models import Count
from django.http import JsonResponse
from rest_framework.views import APIView
from Ausentismo.api.serializer import *
from django.shortcuts import get_object_or_404
from Ausentismo.api.APIs import get_data_api
from datetime import datetime

# Data para las gráficas del front
class DataGrafricas(APIView):
    def get(self, request):
        
        days = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']

        permisos_data = Permisos.objects.values('id', 'codigo_permiso', 'fecha_inicio', 'fecha_incorporacion')
        incapacidades_data = Incapacidades.objects.values('id', 'radicado', 'fecha_inicio', 'fecha_incorporacion')
        
        contador_dias_permisos = {day: 0 for day in days}
        contador_dias_incapacidades = {day: 0 for day in days}

        data_permi = []
        for permisos in permisos_data:
            codigo = permisos.get('codigo_permiso')
            permiso_day_i = permisos.get('fecha_inicio')
            permiso_day_f = permisos.get('fecha_incorporacion')
            
            if permiso_day_i and permiso_day_f:
                days_pass = (permiso_day_f - permiso_day_i).days
                if days_pass == 0:
                    days_pass = 0
                dia_semana = days[permiso_day_i.weekday()]
                contador_dias_permisos[dia_semana] += 1
                
                data_permi.append({
                    'codigo_permiso': codigo,
                    'dias_pass': days_pass,
                })
                
        data_days_i = []  
        for incapacidad in incapacidades_data:
            in_radicado = incapacidad.get('radicado')
            incapacidad_day_i = incapacidad.get('fecha_inicio')
            incapacidad_day_f = incapacidad.get('fecha_incorporacion')
            
            if incapacidad_day_i and incapacidad_day_f:
                days_pass = (incapacidad_day_f - incapacidad_day_i).days
                if days_pass == 0:
                    days_pass = 0
                dia_semana_i = days[incapacidad_day_i.weekday()]
                contador_dias_incapacidades[dia_semana_i] += 1
                
                data_days_i.append({
                    'radicado': in_radicado,
                    'dias_pass': days_pass,
                })

        graficas_response = {
            'permisos': {
                'contador': contador_dias_permisos,
                'data': data_permi
            },
            'incapacidades': {
                'contador': contador_dias_incapacidades,
                'data': data_days_i,
            }
        }
        
        return JsonResponse(graficas_response, status=200, safe=False)
