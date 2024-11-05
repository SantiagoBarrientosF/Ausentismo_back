from Ausentismo.models import *
from Ausentismo.api.serializer import *
from django.http import JsonResponse,HttpResponse
from rest_framework.views import APIView
from django.http import JsonResponse 
from django.http import HttpResponse
import pandas as pd
import io
from collections import defaultdict,Counter
from Ausentismo.api.APIs import get_data_api,get_data_api_Gestiones
from django.http import HttpResponse
from datetime import datetime
import os
from django.core.files.storage import FileSystemStorage
from server.settings import MEDIA_ROOT

class Incapacidadesdata(APIView):
   def get(self,request):    
      incapacidades = Incapacidades.objects.all()
      incapacidades_list = list(incapacidades.values())
      return JsonResponse({'data':incapacidades_list}, safe=False) 
   def post(self,request):
      directory_path = os.path.join(settings.MEDIA_ROOT,)
      fs = FileSystemStorage(location=directory_path)
      protocol = 'http'
      domain = 'localhost:8000'
      base_url = f'{protocol}://{domain}'
      
      if request.method == 'POST':
         # Se obtiene el valor de 'cedula' del cuerpo de la solicitud
         cedula = request.data.get("cedula")
         tipo_gestion = "Incapacidad"
         # Se llama a la función 'get_data_api' para obtener datos adicionales de una API externa
      try:
            datos_api = get_data_api(cedula) 
            Gestion_permisos_api = get_data_api_Gestiones(cedula,"Incapacidad") 
            # Se extraen datos específicos de la respuesta de la API
            nombre= datos_api.get('Nombre')
            campana= datos_api.get('Campaña')
            cargo= datos_api.get('Cargo')
            sede= datos_api.get('Sede')
            turno= request.data.get('turno')
            jefe= request.data.get('jefe')
            fecha_inicio_incapacidad = request.data.get('fecha_inicio_incapacidad')
            fecha_terminacion_incapacidad = request.data.get('fecha_terminacion_incapacidad')   
            fecha_incorporacion = request.data.get('fecha_incorporacion')
            lider= User.objects.get(id=jefe)
            doc_incapacidad = request.FILES.get('doc_incapacidad')
            radicado = request.data.get("radicado")

            fecha_inicio_incapacidad = datetime.strptime(fecha_inicio_incapacidad, '%Y-%m-%d').date()
            fecha_incorporacion = datetime.strptime(fecha_incorporacion, '%Y-%m-%d').date()
            fecha_terminacion_incapacidad = datetime.strptime(fecha_terminacion_incapacidad, '%Y-%m-%d').date()
            
            # Guardar el archivo
            if doc_incapacidad:
                filename = fs.save(doc_incapacidad.name, doc_incapacidad)
                file_url = fs.url(filename)
            else:
                return JsonResponse({"message": "No se proporcionó archivo de incapacidad"}, status=400)
                
            # Se obtienen más valores del cuerpo de la solicitud
            # Verifica que todos los campos requeridos tengan datos válidos
            if nombre and sede and turno and campana and cargo and lider and doc_incapacidad and jefe and lider and cedula:
            # Crear una nueva instancia del modelo 'Permisos' con los datos proporcionados
               data = Incapacidades(
                  cedula=cedula,
                  nombre=nombre,
                  campana=campana,
                  cargo=cargo,
                  sede=sede,
                  turno=turno,
                  lider=lider,
                  doc_incapacidad=f"{base_url}{file_url}",
                  radicado = radicado,
                  fecha_inicio_incapacidad = fecha_inicio_incapacidad,
                  fecha_terminacion_incapacidad = fecha_terminacion_incapacidad,
                  fecha_incorporacion = fecha_incorporacion
               )
            # Guardar el nuevo registro en la base de datos
               data.save()   
              
               # Obtener el último registro guardado de la tabla 'Permisos'
               ultimo_usuario = Incapacidades.objects.last()
               # Serializar ese objeto usando el serializador correspondiente (Permisoserializar)
               serializer_usuario = Incapacidadesserializar(ultimo_usuario) 
               # Retornar la información del último registro en formato JSON junto con un mensaje de éxito
               return JsonResponse({"message":serializer_usuario.data},status=200)
            else:
               return JsonResponse({"message": "Faltan datos"}, status=400)
      except Exception as e:
            return JsonResponse({"message":f"Ocurrió un error durante la solicitud:{str(e)}","status" : 404},status = 404)

def Contarincapacidades_individual(self):
      incapacidades = Permisos.objects.filter(tipo_permiso__in=["Licencia remunerada", "Licencia no remunerada"])
      incapacidad_por_campaña = defaultdict(Counter)
      for incapacidad in incapacidades:
         incapacidad_por_campaña[incapacidad.campana][incapacidad.nombre] += 1
      return JsonResponse(dict(incapacidad_por_campaña),safe=False)
   
def Contarincapacidades_campaña(self,id):
      lider = User.objects.get(id=id)
      jefe_campana = lider.last_name
      incapacidades = Incapacidades.objects.filter(campana = jefe_campana)
      incapacidad_por_campaña = defaultdict(Counter)
      for incapacidad in incapacidades:
         incapacidad_por_campaña[incapacidad.campana][incapacidad.campana]+= 1
      return JsonResponse(dict(incapacidad_por_campaña),safe=False)


class DescargarArchivoView(APIView):
   def get(self, request, nombre_archivo):
      file_path = os.path.join(MEDIA_ROOT, nombre_archivo)
      if os.path.exists(file_path):
         with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
            return response
      else:
            return HttpResponse("Archivo no encontrado.")
      

      # cambio de estados pendiente a otros 3 dependiendo de donde fue sacado es decir eps,ips o consultorio externo