from Ausentismo.models import *
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from Ausentismo.api.serializer import *
from Ausentismo.api.permisos import get_data_api
from django.shortcuts import get_object_or_404
from datetime import date

class vacacionessdata(APIView):
   authentication_classes = [TokenAuthentication]
   permission_classes = [IsAuthenticated]
   def get(self,request):    
      Valor= Vacaciones.objects.all() 
      Valores_list = list(Valor.values())
      return JsonResponse(Valores_list, safe=False) 
   def post(self,request): 
      if request.method == 'POST':
         actual_date = date.today()
         cedula = request.data.get("cedula")
         try:
            datos_api = get_data_api(cedula)
            nombre = datos_api.get('Nombre')
            fecha_ingreso_empresa = datos_api.get('Fecha_ingreso')
            campaña = datos_api.get('Campaña')
            cargo = datos_api.get('Cargo')
            fecha_peticion = date.today()
            correo = request.data.get('correo')
            dias_vacaciones = request.data.get("Dias_habiles")
            periodo = request.data.get("Periodo")
            fecha_inicio = request.data.get('fecha_inicio')
            fecha_incorporacion = request.data.get('fecha_incorporacion')
            observaciones = request.data.get('Observaciones')
            jefe = request.data.get('jefe')
            Jefe_id = User.objects.get(id=jefe)
            if nombre and correo and fecha_ingreso_empresa  and campaña and cargo  and fecha_inicio and fecha_incorporacion and observaciones and jefe and fecha_peticion:
         # Crear una nueva instancia del modelo 'Vacaciones' con los datos proporcionados  
               data  = Vacaciones(
                  cedula = cedula,
                  nombre = nombre,
                  correo = correo,
                  fecha_ingreso_empresa = fecha_ingreso_empresa,
                  campana = campaña,
                  cargo = cargo,
                  fecha_peticion = fecha_peticion,
                  dias_vacaciones = dias_vacaciones,
                  fecha_inicio = fecha_inicio,
                  fecha_incorporacion = fecha_incorporacion,
                  observaciones = observaciones,
                  periodo = periodo,
                  Jefe_id = Jefe_id,
               )
               data.save()
               ultimo_usuario = Vacaciones.objects.last()
               serializer_usuario = Vacacioneserializar(ultimo_usuario)
               return JsonResponse({'data': serializer_usuario.data, 'message': 'Datos agregados correctamente',"status":200},status = 200)
         except Exception as e:
               print(f"error: {e}")
               return JsonResponse({"message":"No se encontro el usuario", "status" : 404},status = 404)
   def put(self,request,id):
      observacion = get_object_or_404(Vacaciones,id=id)
      observacion.observaciones = request.data.get("observaciones")
      observacion.estado = request.data.get("estado")
      observacion.save()
      return JsonResponse({"message":"Datos actualizados correctamente","status":200},status = 200)
   
def filtrar_campañas_vacaciones(request,id):
      try:
         jefe = User.objects.get(id=id)
      except User.DoesNotExist:
         return JsonResponse({'error': 'Jefe no encontrado'}, status=404)
      campaña_jefe = jefe.last_name 
      vacaciones_campañas = Vacaciones.objects.filter(campana=campaña_jefe)
      vacaciones_list = list(vacaciones_campañas.values())
      return JsonResponse({"data":vacaciones_list})



