from collections import defaultdict
from django.db.models import Count
from Ausentismo.models import Permisos, Vacaciones, Tiquetera, Incapacidades
from rest_framework.views import APIView
from django.http import JsonResponse

class DataGestiones(APIView): 
    def get(self, request):
        
        valores_a_contar = ['Negado', 'Aceptado']
        
        # consultas query a los objetos de la bd
        permisos = Permisos.objects.filter(estado__in=valores_a_contar).values('estado').annotate(count=Count('id'))
        vacaciones = Vacaciones.objects.filter(estado__in=valores_a_contar).values('estado').annotate(count=Count('id'))
        tiqueteras = Tiquetera.objects.filter(estado__in=valores_a_contar).values('estado').annotate(count=Count('id'))
        incapacidades = Incapacidades.objects.filter(estado__in=valores_a_contar).values('estado').annotate(count=Count('id'))
        
        # diccionarios de los contadores
        permisos_count = defaultdict(int)
        vacaciones_count = defaultdict(int)
        tiqueteras_count = defaultdict(int)
        incapacidades_count = defaultdict(int)
        
        for permiso in permisos:
            permisos_count[permiso['estado']] = permiso['count']
        
        for vacacion in vacaciones:
            vacaciones_count[vacacion['estado']] = vacacion['count']
            
        for tiquetera in tiqueteras:
            tiqueteras_count[tiquetera['estado']] = tiquetera['count']

        for incapacidad in incapacidades:
            incapacidades_count[incapacidad['estado']] = incapacidad['count']
        
        total_permisos = sum(permisos_count.values())  
        total_vacaciones = sum(vacaciones_count.values())  
        total_tiqueteras = sum(tiqueteras_count.values())  
        total_incapacidades = sum(incapacidades_count.values())  
        
        # permisos
        permisos_calculo = {
            'Negado': {
                'cantidad': permisos_count['Negado'], 
                'Porcentaje': round((permisos_count['Negado'] * 100) / total_permisos, 2)
            } if 'Negado' in permisos_count and total_permisos > 0 else {
                'cantidad': 0,
                'Porcentaje': 0
            },
            'Aceptado': {
                'cantidad': permisos_count['Aceptado'], 
                'Porcentaje': round((permisos_count['Aceptado'] * 100) / total_permisos, 2)
            } if 'Aceptado' in permisos_count and total_permisos > 0 else {
                'cantidad': 0,
                'Porcentaje': 0
            },
            'total_Permisos': total_permisos if total_permisos > 0 else {0}
        }
        
        # vacaciones
        vacaciones_calculo = {
            'Negado': {
                'cantidad': vacaciones_count['Negado'],
                'Porcentaje': round((vacaciones_count['Negado'] * 100) / total_vacaciones, 2)
            } if 'Negado' in vacaciones_count and total_vacaciones > 0 else {
                'cantidad': 0,
                'Porcentaje': 0
            },
            'Aceptado': {
                'cantidad': vacaciones_count['Aceptado'],
                'Porcentaje': round((vacaciones_count['Aceptado'] * 100) / total_vacaciones, 2)
            } if 'Aceptado' in vacaciones_count and total_vacaciones > 0 else {
                'cantidad': 0,
                'Porcentaje': 0
            },
            'total_Vacaciones': total_vacaciones if total_vacaciones > 0 else {0} 
        }
        
        # tiqueteras
        tiqueteras_calculo = {
            'Negado': {
                'cantidad': tiqueteras_count['Negado'],
                'Porcentaje': round((tiqueteras_count['Negado'] * 100) / total_tiqueteras, 2)
            } if 'Negado' in tiqueteras_count and total_tiqueteras > 0 else {
                'cantidad': 0,
                'Porcentaje': 0
            },
            'Aceptado': {
                'cantidad': tiqueteras_count['Aceptado'],
                'Porcentaje': round((tiqueteras_count['Aceptado'] * 100) / total_tiqueteras, 2)
            } if 'Aceptado' in tiqueteras_count and total_tiqueteras > 0 else {
                'cantidad': 0,
                'Porcentaje': 0
            },
            'total_Tiquetera': total_tiqueteras if total_tiqueteras > 0 else {0} 
        }
        
        # incapacidades
        incapacidades_calculo = {
            'Negado': {
                'cantidad': incapacidades_count['Negado'],
                'Porcentaje': round((incapacidades_count['Negado'] * 100) / total_incapacidades, 2)
            } if 'Negado' in incapacidades_count and total_incapacidades > 0 else {
                'cantidad': 0,
                'Porcentaje': 0
            },
            'Aceptado': {
                'cantidad': incapacidades_count['Aceptado'],
                'Porcentaje': round((incapacidades_count['Aceptado'] * 100) / total_incapacidades, 2)
            } if 'Aceptado' in incapacidades_count and total_incapacidades > 0 else {
                'cantidad': 0,
                'Porcentaje': 0
            },
            'total_Incapacidades': total_incapacidades if total_incapacidades > 0 else {0} 
        }
        
        return JsonResponse({
            'Permisos': permisos_calculo,
            'Vacaciones': vacaciones_calculo,
            'Tiquetera': tiqueteras_calculo,
            'Incapacidades': incapacidades_calculo,
        }, status = 200)