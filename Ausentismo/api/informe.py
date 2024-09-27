from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from Ausentismo.api.serializer import *
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
class InformePermisos(APIView):
    def get(self,request):
        return JsonResponse({"message":"sapos"})
class InformeVacaciones(APIView):
    def get(self,request):
        return JsonResponse({"message":"sapos"})
class Informeincapacidades(APIView):
    def get(self,request):
        return JsonResponse({"message":"sapos"})