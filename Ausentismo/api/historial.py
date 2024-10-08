from Ausentismo.models import * 
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from Ausentismo.api.serializer import *
from django.shortcuts import get_object_or_404
class Historialdata(APIView):
 def get(self,request):
     
     return JsonResponse({"message":"Datos "},status = 200)