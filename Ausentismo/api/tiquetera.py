from Ausentismo.models import *
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from Ausentismo.api.serializer import *
from datetime import date
from Ausentismo.api.permisos import get_data_api

class Tiqueteradata(APIView):
#    authentication_classes = [TokenAuthentication]
#    permission_classes = [IsAuthenticated]
   def get(self,request):    
      Valor= Tiquetera.objects.all() 
      Valores_list = list(Valor.values())
      return JsonResponse(Valores_list, safe=False) 
  
   def post(self,request):
      if request.method == 'POST':
         cedula = request.data.get("cedula")
         datos_api = get_data_api(cedula)
         if not datos_api:
            return JsonResponse({"message":"No se encontro el usuario"})
         nombre= datos_api.get('Nombre')
         campaña = datos_api.get('Campaña')
         fecha_peticion = date.today()
         estado = request.data.get('estado')
         beneficios = request.data.get('beneficios')
         jefe = request.data.get('jefe')
         sede = request.data.get('sede')
         tipo_tiquetera = request.data.get('tipo_tiquetera')
         print(request.data)
      if nombre and estado and beneficios  and campaña and fecha_peticion and sede and tipo_tiquetera and jefe:
         data  = Tiquetera(
               cedula = cedula,
               nombre = nombre,
               campaña = campaña,
               fecha_peticion = fecha_peticion,
               estado = estado,
               beneficios = beneficios,
               sede = sede,
               jefe = jefe,
               tipo_tiquetera = tipo_tiquetera
         )
         data.save()
         ultimo_usuario = Tiquetera.objects.last()
         serializer_usuario = Tiqueteraserializar(ultimo_usuario)
         return JsonResponse({'data': serializer_usuario.data, 'message': 'Datos agregados correctamente'})


