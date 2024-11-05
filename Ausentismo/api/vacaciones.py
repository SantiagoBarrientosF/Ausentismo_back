from Ausentismo.models import Vacaciones
from django.http import JsonResponse
from rest_framework.views import APIView
from django.contrib.auth.models import User
from Ausentismo.api.serializer import Vacacioneserializar
from Ausentismo.api.APIs import get_data_api,get_data_api_Gestiones
from django.shortcuts import get_object_or_404
from datetime import date
from django.db.models import Case,When,CharField
from Ausentismo.api.email import enviar_correo_asesor,enviar_correo_lider
from collections import defaultdict
from django.db.models import Count
from datetime import datetime
class vacacionessdata(APIView):
   def get(self,request):    
      Valor= Vacaciones.objects.all() 
      Valores_list = list(Valor.values())
      return JsonResponse(Valores_list, safe=False) 
   def post(self,request): 
      if request.method == 'POST':
         # Se obtiene el valor de 'cedula' del cuerpo de la solicitud
         cedula = request.data.get("cedula")
         
         # Se llama a la función 'get_data_api' para obtener datos adicionales de una API externa
      try:
            datos_api = get_data_api(cedula) 
            Gestiones_vacaciones = get_data_api_Gestiones(cedula,"Vacaciones") 
            # Se extraen datos específicos de la respuesta de la API
            nombre = datos_api.get('Nombre')
            fecha_ingreso_empresa = datos_api.get('Fecha_ingreso')
            campana = datos_api.get('Campaña')
            cargo = datos_api.get('Cargo')
            # Se obtienen más valores del cuerpo de la solicitud
            correo = request.data.get('correo')
            fecha_peticion = date.today()  # Fecha actual de la petición
            fecha_inicio = request.data.get("fecha_inicio")  # Fecha de inicio
            fecha_incorporacion = request.data.get('fecha_incorporacion')
            fecha_terminacion = request.data.get('Fecha_Terminacion')
            jefe = request.data.get('jefe')
            dias_vacaciones = request.data.get('Dias_habiles')
            observaciones = request.data.get('Observaciones')
            periodo = request.data.get('Periodo')
            Jefe_id = User.objects.get(id=jefe)
            # Cambiar formato de la fecha
            fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d').date()
            fecha_incorporacion = datetime.strptime(fecha_incorporacion, '%Y-%m-%d').date()
            fecha_terminacion = datetime.strptime(fecha_terminacion, '%Y-%m-%d').date()
            # Verifica que todos los campos requeridos tengan datos válidos
            if nombre and correo and fecha_ingreso_empresa and campana and cargo and fecha_peticion and fecha_incorporacion and jefe and dias_vacaciones:
            # Crear una nueva instancia del modelo 'Permisos' con los datos proporcionados
               data = Vacaciones(
                  cedula=cedula,
                  nombre=nombre,
                  correo=correo,
                  fecha_ingreso_empresa=fecha_ingreso_empresa,
                  campana=campana,
                  cargo=cargo,
                  fecha_peticion=fecha_peticion,
                  fecha_inicio=fecha_inicio,
                  fecha_incorporacion=fecha_incorporacion,
                  fecha_terminacion=fecha_terminacion,
                  periodo=periodo,
                  Jefe_id=Jefe_id,
                  dias_vacaciones = dias_vacaciones,
                  observaciones = observaciones
            )
            # Guardar el nuevo registro en la base de datos
               data.save()   
               #  Enviar correo
               solicitudes ={
                  'nombre': nombre,
                  'tipo_gestion': "vacaciones",
                  'codigo_vacaciones': data.Codigo_vacaciones
               }  
               to_email = [correo]
               enviar_correo_asesor(to_email,solicitudes)
               #envio del correo al lider
               solicitudes ={
               'nombre': nombre,
               'correo': correo,
               'fecha_ingreso_empresa': fecha_ingreso_empresa,
               'campana': campana,
               'cargo': cargo,
               'fecha_inicio': fecha_inicio,
               'fecha_incorporacion': fecha_incorporacion,
               'Jefe_id': Jefe_id.first_name,
               'dias_vacaciones': dias_vacaciones,
               'tipo_gestion': "vacaciones",
               }
               to_email_lider = [correo]
               enviar_correo_lider(to_email_lider,solicitudes,)
               # Obtener el último registro guardado de la tabla 'Permisos'
               ultimo_usuario = Vacaciones.objects.last()
               # Serializar ese objeto usando el serializador correspondiente (Permisoserializar)
               serializer_usuario = Vacacioneserializar(ultimo_usuario) 
               # Retornar la información del último registro en formato JSON junto con un mensaje de éxito
               return JsonResponse({'data': serializer_usuario.data, 'message': 'Datos agregados correctamente', "status":200})
      except Exception as e:
            return JsonResponse({"message":f"Ocurrió un error durante la solicitud :{str(e)}","status" : 404},status = 404)
   def put(self,request,id):
      observacion = get_object_or_404(Vacaciones,id=id)
      observacion.observaciones = request.data.get("observaciones")
      observacion.estado = request.data.get("estado")
      observacion.save()
      if observacion.estado == "Aprobado":
        solicitudes = {
            'nombre': observacion.nombre,
            'tipo_gestion': "permiso",
            'estado': "aprobado"
        }
        enviar_correo_asesor([observacion.correo], solicitudes)
      else:
        solicitudes = {
            'nombre': observacion.nombre,
            'tipo_gestion': "permiso",
            'estado': "negado"
        }
        enviar_correo_asesor([observacion.correo], solicitudes)
      return JsonResponse({"message":"Datos actualizados correctamente","status":200},status = 200)
   
def filtrar_campañas_vacaciones(request,id):
      try:
         jefe = User.objects.get(id=id)
      except User.DoesNotExist:
         return JsonResponse({'error': 'Jefe no encontrado'}, status=404)
      campaña_jefe = jefe.last_name
      vacaciones_campañas = Vacaciones.objects.filter(campana=campaña_jefe).annotate(permisos_pendientes=Case(When(estado="Pendiente",then=0),default=1,output_field=CharField(),)).order_by('permisos_pendientes')
      vacaciones_list = list(vacaciones_campañas.values())
      return JsonResponse({"data":vacaciones_list})
# Obtener el numero de peticiones de vacaciones cuyo estado sea Aceptado o Negado
def obtener_vacaciones(request):
   permisos_a_contar = ['Negado', 'Aceptado']
   
   permisos = Vacaciones.objects.filter(estado__in=permisos_a_contar).values('estado').annotate(count=Count('id'))
   
   permisos_count = defaultdict(int)
   
   for permiso in permisos:
      permisos_count[permiso['estado']] = permiso['count']
   
   permisos_negados = {'Negado': permisos_count['Negado']} if 'Negado' in permisos_count else {}
   permisos_aceptados = {'Aceptado': permisos_count['Aceptado']} if 'Aceptado' in permisos_count else {}
   
   return JsonResponse({
      'permisos negados': permisos_negados,
      'permisos aceptados': permisos_aceptados,
      'total permisos': str(sum(permisos_count.values()))
   }, status=200)
   