from Ausentismo.models import *
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from Ausentismo.api.serializer import *
from Ausentismo.api.permisos import get_data_api
class vacacionessdata(APIView):
#    authentication_classes = [TokenAuthentication]
#    permission_classes = [IsAuthenticated]
   def get(self,request):    
      Valor= Vacaciones.objects.all() 
      Valores_list = list(Valor.values())
      return JsonResponse(Valores_list, safe=False) 
  
   def post(self,request):
      # Users = User.objects.filter(is_superadmin = True)
      
      if request.method == 'POST':
         cedula = request.data.get("cedula")
         try:
          Codigo_vacacione = request.data.get("codigo")
          datos_api = get_data_api(cedula)
          nombre = datos_api.get('Nombre')
          correo = request.data.get('correo')
          fecha_ingreso_empresa = datos_api.get('Fecha_ingreso')
          campaña = datos_api.get('Campaña')
          cargo = datos_api.get('Cargo')
          fecha_inicio = request.data.get("fecha_inicio")
          fecha_fin = request.data.get('fecha_fin')
          fecha_incorporacion = request.data.get('fecha_incorporacion')
          observaciones = request.data.get('observaciones')
          jefe = request.data.get('jefe')
          
          print(request.data)
          if nombre and correo and fecha_ingreso_empresa  and campaña and cargo and fecha_inicio and fecha_fin and fecha_incorporacion and observaciones and jefe:
           data  = Vacaciones(
                cedula = cedula,
                Codigo_vacacione = Codigo_vacacione,
                nombre = nombre,
                correo = correo,
                fecha_ingreso_empresa = fecha_ingreso_empresa,
                campaña = campaña,
                cargo = cargo,
                fecha_inicio = fecha_inicio,
                fecha_fin = fecha_fin,
                fecha_incorporacion = fecha_incorporacion,
                observaciones = observaciones,
                jefe = jefe,
           )
           data.save()
           ultimo_usuario = Vacaciones.objects.last()
           serializer_usuario = Vacacioneserializar(ultimo_usuario)
           return JsonResponse({'data': serializer_usuario.data, 'message': 'Datos agregados correctamente'})
         except:
            return JsonResponse({"message":"No se encontro el usuario"},status = 404)
 



