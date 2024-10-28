from Ausentismo.models import *
from Ausentismo.api.serializer import *
from django.http import JsonResponse,HttpResponse
from rest_framework.views import APIView
from django.http import JsonResponse 
from django.http import HttpResponse
import pandas as pd
import io
from collections import defaultdict,Counter
from Ausentismo.api.permisos import get_data_api,get_data_api_Gestiones
from django.http import HttpResponse

class Incapacidadesdata(APIView):
   def get(self,request):    
      incapacidades = Incapacidades.objects.all()
      incapacidades_list = list(incapacidades.values())
      return JsonResponse(incapacidades_list, safe=False) 
   def post(self,request):
      if request.method == 'POST':
         # Se obtiene el valor de 'cedula' del cuerpo de la solicitud
         cedula = request.data.get("cedula")
         tipo_gestion = "Incapacidad"
         # Se llama a la función 'get_data_api' para obtener datos adicionales de una API externa
      try:
            datos_api = get_data_api(cedula) 
            Gestion_permisos_api = get_data_api_Gestiones(cedula,tipo_gestion) 
            # Se extraen datos específicos de la respuesta de la API
            nombre= datos_api.get('Nombre')
            campana= datos_api.get('Campaña')
            cargo= datos_api.get('Cargo')
            sede= datos_api.get('Sede')
            turno= request.data.get('turno')
            jefe= request.data.get('jefe')
            lider= User.objects.get(id=jefe)
            doc_incapacidades = request.FILES.get('doc_incapacidades')
            radicado = request.data.get("radicado")
            print(doc_incapacidades)
            # Se obtienen más valores del cuerpo de la solicitud
            # Verifica que todos los campos requeridos tengan datos válidos
            if nombre and sede and turno and campana and cargo and lider and doc_incapacidades and jefe and lider and cedula:
            # Crear una nueva instancia del modelo 'Permisos' con los datos proporcionados
               data = Incapacidades(
                  cedula=cedula,
                  nombre=nombre,
                  campana=campana,
                  cargo=cargo,
                  sede=sede,
                  turno=turno,
                  lider=lider,
                  doc_incapacidad=doc_incapacidades,
                  radicado = radicado
               )
            # Guardar el nuevo registro en la base de datos
               data.save()   
               print(data)
               # Obtener el último registro guardado de la tabla 'Permisos'
               ultimo_usuario = Incapacidades.objects.last()
               # Serializar ese objeto usando el serializador correspondiente (Permisoserializar)
               serializer_usuario = Incapacidadesserializar(ultimo_usuario) 
               # Retornar la información del último registro en formato JSON junto con un mensaje de éxito
               return JsonResponse({"message":serializer_usuario},status=200)
            else:
               return JsonResponse({"message": "No se pudieron guardar los datos"}, status=400)
      except Exception as e:
            return JsonResponse({"message":f"Ocurrió un error durante la solicitud:{str(e)}","status" : 404},status = 404)

def export_incapacidades(self,id):
   incapacidad = Incapacidades.objects.filter(lider_id = id)
   datos = []
   for solicitud in incapacidad:
      datos.append({
         "Radicado incapacidad":solicitud.radicado,
         "Cedula": solicitud.cedula,
         "Nombre": solicitud.nombre,
         "Cargo": solicitud.cargo,
         "Campaña": solicitud.campana,
         "Fecha inicio incapacidad": solicitud.fecha_inicio,
         "Fecha fin incapacidad": solicitud.fecha_incorporacion,
      })
   df = pd.DataFrame(datos)
   output  = io.BytesIO()
   with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False)
   response = HttpResponse(output.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
   response['Content-Disposition'] = 'attachment; filename=Informe_incapacidades.xlsx'
   return response

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
