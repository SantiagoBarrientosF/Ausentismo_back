from Ausentismo.models import *
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from Ausentismo.api.serializer import *
from datetime import date

class Permisosdata(APIView):
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
          correo = request.data.get("correo")    
          fecha_ingreso_empresa = request.data.get("fecha_ingreso")
          fecha_peticion = date.today()
          campaña = request.data.get("campania")
          cargo = request.data.get("cargo")
          fecha_incorporacion = request.data.get("fecha_incorporacion")
          observaciones = request.data.get("observaciones")
          jefe = request.data.get("jefe")
          tipo_permiso = request.data.get("tipo_permiso")
          print(request.data)
      if cedula and nombre and correo and fecha_ingreso_empresa and tipo_permiso and campaña and cargo and fecha_incorporacion and observaciones and jefe :
          data  = Permisos(
             cedula = cedula,
             nombre = nombre,
             correo = correo,
             fecha_ingreso_empresa = fecha_ingreso_empresa,
             fecha_peticion = fecha_peticion,
             campaña = campaña,
             cargo = cargo,
             fecha_incorporacion = fecha_incorporacion,
             observaciones = observaciones,
             jefe = jefe,
             tipo_permiso = tipo_permiso,
            )
          data.save()
          ultimo_permiso = Permisos.objects.last()
          serializer_permiso = Permisoserializar(ultimo_permiso)
          return JsonResponse({'data': serializer_permiso.data, 'message': 'Datos agregados correctamente'})





