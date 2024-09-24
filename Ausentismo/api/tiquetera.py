from Ausentismo.models import *
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from Ausentismo.api.serializer import *
from datetime import date

class Tiqueteradata(APIView):
#    authentication_classes = [TokenAuthentication]
#    permission_classes = [IsAuthenticated]
   def get(self,request):    
      Valor= Permisos.objects.all() 
      Valores_list = list(Valor.values())
      return JsonResponse(Valores_list, safe=False) 
  
   def post(self,request):
       
      if request.method == 'POST':
          cedula = request.data.get("cedula")
          nombre = request.data.get("nombre")
          campaña = request.data.get("campaña")    
          jefe = request.data.get("fecha_ingreso")
          fecha_peticion = date.today()
          estado = request.data.get("campania")
          beneficios = request.data.get("cargo")
          tipo_tiquetera = request.data.get("tipo_tiquetera")
          print(request.data)
      if cedula and nombre and estado and beneficios and campaña and jefe :
          data  = Tiquetera(
             cedula = cedula,
             nombre = nombre,
             campaña = campaña,
             fecha_peticion = fecha_peticion,
             tipo_permiso = tipo_tiquetera,
             beneficios = beneficios,
             estado = estado,
            )
          data.save()
          ultimo_permiso = Permisos.objects.last()
          serializer_permiso = Permisoserializar(ultimo_permiso)
          return JsonResponse({'data': serializer_permiso.data, 'message': 'Datos agregados correctamente'})





