from Ausentismo.models import Permisos
from rest_framework.views import APIView
from Ausentismo.api.serializer import *
from datetime import date
from django.contrib.auth.models import User
from Ausentismo.api.email import *
from django.shortcuts import get_object_or_404
from django.db.models import Case,When,CharField
from rest_framework.response import Response
from django.http import JsonResponse
from Ausentismo.api.email import enviar_correo_asesor,enviar_correo_lider
from Ausentismo.api.APIs import get_data_api,get_data_api_Gestiones

# Vista basada en clases para manejar datos de permisos
class Permisosdata(APIView):
  # Método GET para obtener todos los registros del modelo 'Permisos'
  def get(self, request):
      # Se obtienen todos los objetos de la tabla 'Permisos'
      Valor = Permisos.objects.all()
      # Se convierte el queryset a una lista de diccionarios con los valores de cada objeto
      Valores_list = list(Valor.values())
      # Se devuelve la lista en formato JSON, permitiendo que sea una lista gracias a 'safe=False'
      return JsonResponse({'data': Valores_list}, status = 200,  safe=False)
      # return Response(Valores_list)
  # Método POST para agregar un nuevo registro en la tabla 'Permisos'
  def post(self, request):
    # Verificar que el método sea POST
    if request.method == 'POST':
        # Se obtiene el valor de 'cedula' del cuerpo de la solicitud
      cedula = request.data.get("cedula")
        # Se llama a la función 'get_data_api' para obtener datos adicionales de una API externa
      try:
          datos_api = get_data_api(cedula) 
          Gestiones_permisos = get_data_api_Gestiones(cedula,"Permiso") 
          if not datos_api:
            return JsonResponse({"message":"No se pudo encontrar el usuario"}, status=404)
          # Se extraen datos específicos de la respuesta de la API
          nombre = datos_api.get('Nombre')
          fecha_ingreso_empresa = datos_api.get('Fecha_ingreso')
          campana = datos_api.get('Campaña')
          cargo = datos_api.get('Cargo')
          # Se obtienen más valores del cuerpo de la solicitud
          correo = request.data.get('correo')
          fecha_peticion = date.today()  # Fecha actual de la petición
          fecha_inicio = request.data.get("fecha_inicio")  # Fecha de inicio
          fecha_incorporacion = request.data.get('fecha_fin')
          jefe = request.data.get('jefe')
          parentesco = request.data.get('parentesco')
          tipo_permiso = request.data.get('tipo_permiso')
          Jefe_id = User.objects.get(id=jefe)
          # Verifica que todos los campos requeridos tengan datos válidos
          if nombre and correo and fecha_ingreso_empresa and campana and cargo and fecha_peticion and fecha_incorporacion and jefe:
          # Crear una nueva instancia del modelo 'Permisos' con los datos proporcionados
            data = Permisos(
              cedula=cedula,
              nombre=nombre,
              correo=correo,
              fecha_ingreso_empresa=fecha_ingreso_empresa,
              campana=campana,
              cargo=cargo,
              fecha_peticion=fecha_peticion,
              fecha_inicio=fecha_inicio,
              fecha_incorporacion=fecha_incorporacion,
              Jefe_id=Jefe_id,
              parentesco=parentesco,
              tipo_permiso=tipo_permiso
            )
            # Guardar el nuevo registro en la base de datos
            data.save()
            # Envio del correo al asesor
            solicitudes ={
               'nombre': nombre,
               'tipo_gestion': "permiso",
               'codigo_permiso': data.codigo_permiso
            }
            to_email = [correo]
            enviar_correo_asesor(to_email,solicitudes)
            #envio del correo al lider
            solicitudes ={
                    'nombre': nombre,
                    'codigo_permiso': data.codigo_permiso,
                    'cedula': cedula,
                    'correo': correo,
                    'fecha_ingreso': fecha_ingreso_empresa,
                    'campaña': campana,
                    'cargo': cargo,
                    'fecha_inicio': fecha_inicio,
                    'fecha_fin': fecha_incorporacion,
                    'jefe': Jefe_id.first_name,
                    'tipo_permiso': tipo_permiso,
                    'tipo_gestion': "permiso"
            }
            to_email_asesor = [Jefe_id.email]
            enviar_correo_lider(to_email_asesor,solicitudes)
            # retornar la data del registro guardado
            ultimo_permiso = Permisos.objects.last()
            serializer_permisos = Permisoserializar(ultimo_permiso)
            return Response({'data': serializer_permisos.data, 'message': 'Datos agregados correctamente', "status": 200},status = 200)
      except Exception as e:
            return Response({"message": f"Ocurrió un error durante la solicitud: {e}","status" : 404},status = 404)
          
  def put(self,request,id):
      observacion = get_object_or_404(Permisos,id=id)
      observacion.observaciones = request.data.get("observaciones")
      observacion.estado = request.data.get("estado")
      observacion.save()

      if observacion.estado == "Aprobado":
        solicitudes = {
            'nombre': observacion.nombre,
            'tipo_gestion': "permiso",
            'estado': "aprobada"
        }
        enviar_correo_asesor([observacion.correo], solicitudes)
      else:
        solicitudes = {
            'nombre': observacion.nombre,
            'tipo_gestion': "permiso",
            'estado': "rechazada"
        }
        enviar_correo_asesor([observacion.correo], solicitudes)
      return Response({"message":"Datos actualizados correctamente","status":200},status = 200)
    
def filtrar_campañas(request,id):
    try:
        jefe = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response({'error': 'Jefe no encontrado',"status":400}, status=404)
      
    campaña_jefe = jefe.last_name 
    permisos_relacionados = Permisos.objects.filter(campana=campaña_jefe).annotate(permisos_pendientes=Case(When(estado="Pendiente",then=0),default=1,output_field=CharField(),)).order_by('permisos_pendientes')
    permisos_list = list(permisos_relacionados.values())
    return JsonResponse({"data":permisos_list,"status":200},status = 200)
