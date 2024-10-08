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
      if request.method == 'POST':
         cedula = request.data.get("cedula")
         try:
            datos_api = get_data_api(cedula)
            nombre = datos_api.get('Nombre')
            fecha_ingreso_empresa = datos_api.get('Fecha_ingreso')
            campaña = datos_api.get('Campaña')
            cargo = datos_api.get('Cargo')
            fecha_inicio = request.data.get("fecha_inicio")
            correo = request.data.get('correo')
            dias_vacaciones = request.data.get("Dias_habiles")
            periodo = request.data.get("Periodo")
            fecha_fin = request.data.get('Fecha_Terminacion')
            fecha_incorporacion = request.data.get('fecha_incorporacion')
            observaciones = request.data.get('Observaciones')
            jefe = request.data.get('jefe')
            User_id = User.objects.get(id=jefe)
            if nombre and correo and fecha_ingreso_empresa  and campaña and cargo and fecha_inicio and fecha_fin and fecha_incorporacion and observaciones and jefe:
         # Crear una nueva instancia del modelo 'Vacaciones' con los datos proporcionados  
               data  = Vacaciones(
                  cedula = cedula,
                  nombre = nombre,
                  correo = correo,
                  fecha_ingreso_empresa = fecha_ingreso_empresa,
                  campaña = campaña,
                  cargo = cargo,
                  fecha_inicio = fecha_inicio,
                  dias_vacaciones = dias_vacaciones,
                  fecha_fin = fecha_fin,
                  fecha_incorporacion = fecha_incorporacion,
                  observaciones = observaciones,
                  periodo = periodo,
                  User_id = User_id,
               )
               data.save()
               # Crear una nueva instancia del modelo 'Historial_vacaciones' con los datos proporcionados
               data_historial_vacaciones  = Historial_vacaciones(
                  cedula = cedula,
                  nombre = nombre,
                  correo = correo,
                  fecha_ingreso_empresa = fecha_ingreso_empresa,
                  campaña = campaña,
                  cargo = cargo,
                  fecha_inicio = fecha_inicio,
                  dias_vacaciones = dias_vacaciones,
                  fecha_fin = fecha_fin,
                  fecha_incorporacion = fecha_incorporacion,
                  periodo = periodo,
               )
               data_historial_vacaciones.save()
               ultimo_usuario = Vacaciones.objects.last()
               serializer_usuario = Vacacioneserializar(ultimo_usuario)
               return JsonResponse({'data': serializer_usuario.data, 'message': 'Datos agregados correctamente',"status":200},status = 200)
         except Exception as e:
               print(f"error: {e}")
               return JsonResponse({"message":"No se encontro el usuario", "status" : 404},status = 404)
 



