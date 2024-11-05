from Ausentismo.models import Permisos, Tiquetera, Vacaciones, Incapacidades
from django.db.models import Count
from collections import defaultdict
from django.http import JsonResponse
from rest_framework.views import APIView
from Ausentismo.api.serializer import *
from django.shortcuts import get_object_or_404
from Ausentismo.api.APIs import get_data_api
from datetime import datetime

# Data para las gráficas del front
class DataGrafricas(APIView):
    def get(self, request):
        
        # diccionarios de las graficas
        days = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
        months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

        # consultas query a los modelos
        permisos_data = Permisos.objects.values('id', 'codigo_permiso', 'fecha_inicio', 'fecha_incorporacion')
        incapacidades_data = Incapacidades.objects.values('id', 'radicado', 'fecha_inicio_incapacidad', 'fecha_incorporacion')
        tiqueteras_data = Tiquetera.objects.values('id', 'codigo_tiquetera', 'fecha_peticion', 'tipo')
        vacaciones_data = Vacaciones.objects.values('id', 'Codigo_vacaciones', 'dias_vacaciones', 'fecha_inicio','fecha_incorporacion')
        
        # contadores dias
        contador_dias_permisos = {day: 0 for day in days}
        contador_dias_incapacidades = {day: 0 for day in days}
        
        # contadores meses
        cont_mes_i = {month: 0 for month in months}
        cont_mes_v = {month: 0 for month in months}
        cont_mes_p = {month: 0 for month in months}
        cont_mes_t = {month: 0 for month in months}

        for permisos in permisos_data:
            permiso_day_i = permisos.get('fecha_inicio')

            # contador meses
            mes = permiso_day_i.month
            mes_year = months[mes - 1]
            cont_mes_p[mes_year] += 1
            
            # contador dias
            if permiso_day_i:
                dia_semana = days[permiso_day_i.weekday()]
                contador_dias_permisos[dia_semana] += 1
            
        data_days_i = []  
        for incapacidad in incapacidades_data:
            # data para las graficas
            in_radicado = incapacidad.get('radicado')
            incapacidad_day_i = incapacidad.get('fecha_inicio_incapacidad')

            # contador meses
            mes = incapacidad_day_i.month
            mes_year = months[mes - 1]
            cont_mes_i[mes_year] += 1
            incapacidad_day_f = incapacidad.get('fecha_incorporacion')
            
            # contador dias
            if incapacidad_day_i and incapacidad_day_f:
                # se suma 1 al final para un calculo mas acertado
                days_pass = ((incapacidad_day_f - incapacidad_day_i).days) + 1
                if days_pass == 0:
                    days_pass = 0
                dia_semana_i = days[incapacidad_day_i.weekday()]
                contador_dias_incapacidades[dia_semana_i] += 1
                
                # data incapacidades
                data_days_i.append({
                    'radicado': in_radicado,
                    'dias_pass': days_pass,
                })
                
        for tiquetera in tiqueteras_data:
            fecha = tiquetera.get('fecha_peticion')

            # contador meses
            mes = fecha.month
            mes_year = months[mes - 1]
            cont_mes_t[mes_year] += 1
            
        for vacacion in vacaciones_data:
            fecha = vacacion.get('fecha_inicio')

            # contador meses
            mes = fecha.month
            mes_year = months[mes - 1]
            cont_mes_v[mes_year] += 1
            
        # graficas response
        graficas = {
            'dias_incapacidades': {
                'dias': contador_dias_incapacidades,
                'data': data_days_i
                },
            'dias_permisos': contador_dias_permisos,
            'meses_permisos': cont_mes_p,
            'meses_incapacidades': cont_mes_i,
            'meses_vacaciones': cont_mes_v,
            'meses_tiquetera': cont_mes_t
        } 
        
        return JsonResponse(graficas, status=200, safe=False)
