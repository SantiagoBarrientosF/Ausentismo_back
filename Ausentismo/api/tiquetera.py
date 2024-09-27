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

    # Método GET para obtener todos los registros de la tabla Tiquetera
    def get(self, request):    
        # Se obtienen todos los objetos del modelo Tiquetera
        Valor = Tiquetera.objects.all() 
        # Se convierte el queryset en una lista de diccionarios con los valores de cada objeto
        Valores_list = list(Valor.values())
        # Se retorna la lista en formato JSON sin necesidad de serialización (safe=False permite retornar listas)
        return JsonResponse(Valores_list, safe=False) 
  
    # Método POST para agregar un nuevo registro a la tabla Tiquetera
    def post(self, request):
        # Verificar que el método sea POST
        if request.method == 'POST':
            # Se obtiene el valor de 'cedula' del cuerpo de la solicitud
            cedula = request.data.get("cedula")
            # Se hace una llamada a una función externa (get_data_api) para obtener datos adicionales de una API
            datos_api = get_data_api(cedula)
            # Si no se encuentran datos en la API, se retorna un mensaje de error
            if not datos_api:
                return JsonResponse({"message": "No se encontró el usuario"})
            
            # Se extraen datos específicos de la respuesta de la API
            nombre = datos_api.get('Nombre')
            campaña = datos_api.get('Campaña')
            # Se obtiene la fecha actual para la solicitud
            fecha_peticion = date.today()
            # Se extraen otros valores del cuerpo de la solicitud
            estado = request.data.get('estado')
            beneficios = request.data.get('beneficios')
            jefe = request.data.get('jefe')
            sede = request.data.get('sede')
            tipo_tiquetera = request.data.get('tipo_tiquetera')

            # Para depuración, se imprime el contenido del cuerpo de la solicitud
            print(request.data)

        # Verificar que todos los campos requeridos estén presentes
        if nombre and estado and beneficios and campaña and fecha_peticion and sede and tipo_tiquetera and jefe:
            # Crear una nueva instancia del modelo Tiquetera con los datos obtenidos
            data = Tiquetera(
                cedula=cedula,
                nombre=nombre,
                campaña=campaña,
                fecha_peticion=fecha_peticion,
                estado=estado,
                beneficios=beneficios,
                sede=sede,
                jefe=jefe,
                tipo_tiquetera=tipo_tiquetera
            )
            # Guardar el nuevo registro en la base de datos
            data.save()

            # Obtener el último registro guardado en la tabla Tiquetera
            ultimo_usuario = Tiquetera.objects.last()
            # Serializar ese objeto usando el serializador correspondiente (Tiqueteraserializar)
            serializer_usuario = Tiqueteraserializar(ultimo_usuario)

            # Retornar la información del último registro en formato JSON con un mensaje de éxito
            return JsonResponse({'data': serializer_usuario.data, 'message': 'Datos agregados correctamente'})
