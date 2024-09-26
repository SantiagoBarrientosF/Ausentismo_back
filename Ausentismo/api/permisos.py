from Ausentismo.models import *
from django.http import JsonResponse,HttpResponse
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from Ausentismo.api.serializer import *
from datetime import date
from Ausentismo.api.backend import *
# from Ausentismo.api.backend import get_datos_api
import requests
def get_data_api(cedula):
   print("llamando la api..")
   api_url = f"http://127.0.0.1:8001/api/users/{cedula}"
   headers = {
     "accept": "application/json",
     'Connection': 'keep-alive',
   }
    
   print(api_url )
   try:
     response = requests.get(api_url,headers=headers)
     if response.status_code == 200:
       datos = response.json()
       return datos
     else:
       return None
   except requests.exceptions.RequestException as e:
     print(f"Error: {e}")
     return None
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
         datos_api = get_data_api(cedula)
         if not datos_api:
            return JsonResponse({"message":"No se encontro el usuario"})
         nombre= datos_api.get('Nombre')
         correo = request.data.get('correo')
         fecha_ingreso_empresa = datos_api.get('Fecha_ingreso')
         campaña = datos_api.get('Campaña')
         cargo = datos_api.get('Cargo')
         fecha_peticion = date.today()
         fecha_incorporacion = request.data.get('fecha_incorporacion')
         observaciones = request.data.get('observaciones')
         jefe = request.data.get('jefe')
         parentesco = request.data.get('parentesco')
         tipo_permiso = request.data.get('tipo_permiso')
         print(request.data)
      if nombre and correo and fecha_ingreso_empresa  and campaña and cargo and fecha_peticion and fecha_incorporacion and observaciones and jefe:
         data  = Permisos(
               cedula = cedula,
               nombre = nombre,
               correo = correo,
               fecha_ingreso_empresa = fecha_ingreso_empresa,
               campaña = campaña,
               cargo = cargo,
               fecha_peticion = fecha_peticion,
               fecha_incorporacion = fecha_incorporacion,
               observaciones = observaciones,
               jefe = jefe,
               parentesco = parentesco,
               tipo_permiso = tipo_permiso
         )
         data.save()
         ultimo_usuario = Permisos.objects.last()
         serializer_usuario = Permisoserializar(ultimo_usuario)
         return JsonResponse({'data': serializer_usuario.data, 'message': 'Datos agregados correctamente'})




