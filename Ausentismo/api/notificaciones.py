from Ausentismo.models import * 
from Ausentismo.api.permisos import *
from Ausentismo.api.vacaciones import * 
from Ausentismo.api.tiquetera import * 
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from collections import defaultdict,Counter

def Gestion_permisos(request):
    Valor = Permisos.objects.all()
    Valores_list = list(Valor.values())
    return JsonResponse(Valores_list, safe=False)

def Gestion_vacaciones(request):
    Valor = Vacaciones.objects.all()
    Valores_list = list(Valor.values())
    return JsonResponse(Valores_list, safe=False)

def solicitud_incapacidad(request):
    return JsonResponse()