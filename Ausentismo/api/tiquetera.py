from Ausentismo.models import *
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from Ausentismo.api.serializer import *
from datetime import date
from Ausentismo.api.permisos import get_data_api
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

class Tiqueteradata(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

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
        cedula = request.data.get("cedula")
        try:
            datos_api = get_data_api(cedula)
            if not datos_api:
                return JsonResponse({"message":"No se pudo encontrar el usuario"}, status=404)
            nombre = datos_api.get('Nombre')
            correo = request.data.get('correo')
            campana = datos_api.get('Campaña')
            # fecha_peticion = date.today()
            tipo = request.data.get('tipo')
            estado = request.data.get('estado')
            beneficios = request.data.get('beneficio')
            Jefe_id = request.data.get('jefe')
            jefe = User.objects.get(id=Jefe_id)
            data = Tiquetera(
                    cedula = cedula,
                    nombre = nombre,
                    correo = correo,
                    # fecha_peticion = fecha_peticion,
                    campana = campana,
                    tipo = tipo,
                    estado = estado,
                    beneficios = beneficios,
                    Jefe_id = jefe
                )
            data.save()
            
            # Serialize the last added record
            ultimo_usuario = Tiquetera.objects.last()
            serializer_usuario = Tiqueteraserializar(ultimo_usuario)
            return JsonResponse({'data': serializer_usuario.data, 'message': 'Datos agregados correctamente', "status": 200})

        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({"message": f"Error processing request: {str(e)}"}, status=500)

 

class beneficios(APIView):
    def get(self, request):    
        # Se obtienen todos los objetos del modelo Tiquetera
        Valor = beneficios_tiquetera.objects.all() 
        # Se convierte el queryset en una lista de diccionarios con los valores de cada objeto
        Valores_list = list(Valor.values())
        # Se retorna la lista en formato JSON sin necesidad de serialización (safe=False permite retornar listas)
        return JsonResponse(Valores_list, safe=False) 
    def post(self,request):
        try:
            if request.method == "POST":
                beneficio = request.data.get("beneficio")
                horas_disponibles  = 2
                tipo = request.data.get("tipo")
                if beneficio and horas_disponibles and tipo:
                    data = beneficios_tiquetera(
                        beneficio = beneficio,
                        horas_disponibles = horas_disponibles,
                        tipo = tipo
                    )
                    data.save()
                    return JsonResponse({"message":"Datos guardados correctamente"})
        except Exception as e:
            return JsonResponse({"message":"No se pueden guardar los datos"})
        
    def put(self,request,id):
        beneficios_tiqueteras = get_object_or_404(beneficios_tiquetera,id=id)
        beneficios_tiqueteras.beneficio = request.data.get("beneficio")
        beneficios_tiqueteras.save()
        print(beneficios_tiqueteras)
        return JsonResponse({"message": "Registro actualizado con exito", "status":200})