from Ausentismo.models import *
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from Ausentismo.api.serializer import *

class Usersdata(APIView):
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
          dias_vacaciones = request.data.get("dias_vacaciones")
          campaña = request.data.get("campania")
          cargo = request.data.get("cargo")
          fecha_inicio =request.data.get("fecha_inicio")
          fecha_fin = request.data.get("fecha_fin")
          fecha_incorporacion = request.data.get("fecha_incorporacion")
          observaciones = request.data.get("observaciones")
          jefe = request.data.get("jefe")
          print(request.data)
      if cedula and nombre and correo and fecha_ingreso_empresa and dias_vacaciones and campaña and cargo and fecha_inicio and fecha_fin and fecha_incorporacion and observaciones and jefe :
          data  = Permisos(
             cedula = cedula,
             nombre = nombre,
             correo = correo,
             fecha_ingreso_empresa = fecha_ingreso_empresa,
             dias_vacaciones = dias_vacaciones,
             campaña = campaña,
             cargo = cargo,
             fecha_inicio = fecha_inicio, 
             fecha_fin = fecha_fin,
             fecha_incorporacion = fecha_incorporacion,
             observaciones = observaciones,
             jefe = jefe
            )
          data.save()
          ultimas_vacaciones = Vacaciones.objects.last()
          serializer_vacaciones = Vacacioneserializar(ultimas_vacaciones)
          return JsonResponse({'data': serializer_vacaciones.data, 'message': 'Datos agregados correctamente'})





