from Ausentismo.models import *
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from Ausentismo.api.serializer import *
from datetime import date
from Ausentismo.api.backend import *
# from Ausentismo.api.backend import get_datos_api
import requests

# Función para obtener datos de un usuario a través de una API externa, utilizando la 'cedula'
def get_data_api(cedula):
  print("llamando la api..")
  # URL de la API a la que se realiza la solicitud, basada en el valor de 'cedula'
  api_url = f"http://127.0.0.1:8001/api/users/{cedula}"
  headers = {
    "accept": "application/json",
    'Connection': 'keep-alive',
  }
  # Imprime la URL generada para depuración
  print(api_url)

  try:
    # Realiza la solicitud GET a la API con los encabezados definidos
    response = requests.get(api_url, headers=headers)
    # Si la respuesta es exitosa (código 200), devuelve los datos en formato JSON
    if response.status_code == 200:
      datos = response.json()
      print(datos)
      return datos
    else:
      # Si no es exitosa, devuelve 'None'
      return None
  except requests.exceptions.RequestException as e:
    # Maneja cualquier error de la solicitud y lo imprime para depuración
    print(f"Error: {e}")
    return None
# Vista basada en clases para manejar datos de permisos
class Permisosdata(APIView):
  # authentication_classes = [TokenAuthentication]
  # permission_classes = [IsAuthenticated]
  # Método GET para obtener todos los registros del modelo 'Permisos'
  def get(self, request):
      # Se obtienen todos los objetos de la tabla 'Permisos'
      Valor = Permisos.objects.all()
      # Se convierte el queryset a una lista de diccionarios con los valores de cada objeto
      Valores_list = list(Valor.values())
      # Se devuelve la lista en formato JSON, permitiendo que sea una lista gracias a 'safe=False'
      return JsonResponse(Valores_list, safe=False)
  # Método POST para agregar un nuevo registro en la tabla 'Permisos'
  def post(self, request):
    # Verificar que el método sea POST
    if request.method == 'POST':
        # Se obtiene el valor de 'cedula' del cuerpo de la solicitud
      cedula = request.data.get("cedula")
        # Se llama a la función 'get_data_api' para obtener datos adicionales de una API externa
      try:
          datos_api = get_data_api(cedula) 
          # Se extraen datos específicos de la respuesta de la API
          nombre = datos_api.get('Nombre')
          fecha_ingreso_empresa = datos_api.get('Fecha_ingreso')
          campaña = datos_api.get('Campaña')
          cargo = datos_api.get('Cargo')
          
          # Se obtienen más valores del cuerpo de la solicitud
          correo = request.data.get('correo')
          fecha_peticion = date.today()  # Fecha actual de la petición
          fecha_inicio = request.data.get("fecha_inicio")  # Fecha de inicio
          fecha_fin = request.data.get("fecha_fin")  # Fecha de fin
          fecha_incorporacion = request.data.get('fecha_incorporacion')
          jefe = request.data.get('jefe')
          parentesco = request.data.get('parentesco')
          tipo_permiso = request.data.get('tipo_permiso')
          User_id = User.objects.get(id=jefe)
          # Verifica que todos los campos requeridos tengan datos válidos
          if nombre and correo and fecha_ingreso_empresa and campaña and cargo and fecha_peticion and fecha_incorporacion and jefe:
          # Crear una nueva instancia del modelo 'Permisos' con los datos proporcionados
            data = Permisos(
              cedula=cedula,
              nombre=nombre,
              correo=correo,
              fecha_ingreso_empresa=fecha_ingreso_empresa,
              campaña=campaña,
              cargo=cargo,
              fecha_peticion=fecha_peticion,
              fecha_inicio=fecha_inicio,
              fecha_fin=fecha_fin,
              fecha_incorporacion=fecha_incorporacion,
              User_id=User_id,
              parentesco=parentesco,
              tipo_permiso=tipo_permiso
            )
              # Crear una nueva instancia del modelo 'Permisos' con los datos proporcionados
            # Guardar el nuevo registro en la base de datos
            data.save()
            data_historial_permisos = Historial_permisos(
              
              codigo_permiso = data.codigo_permiso,
              cedula = cedula,
              nombre = nombre,
              cargo  = cargo,
              fecha_ingreso_empresa = fecha_ingreso_empresa,
              fecha_fin = fecha_fin,
              fecha_inicio = fecha_inicio,
              tipo_permiso = tipo_permiso,
              fecha_peticion  = fecha_peticion
            )
            data_historial_permisos.save()
            # Obtener el último registro guardado de la tabla 'Permisos'
            ultimo_usuario = Permisos.objects.last()
            # Serializar ese objeto usando el serializador correspondiente (Permisoserializar)
            serializer_usuario = Permisoserializar(ultimo_usuario) 
            # Retornar la información del último registro en formato JSON junto con un mensaje de éxito
            return JsonResponse({'data': serializer_usuario.data, 'message': 'Datos agregados correctamente', "status":200})
      except Exception as e:
            print(f"error{e}")
            return JsonResponse({"message": "Ocurrió un error durante la solicitud","status" : 404})

