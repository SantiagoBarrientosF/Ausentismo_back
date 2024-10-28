from Ausentismo.models import Tiquetera
from django.http import JsonResponse
from rest_framework.views import APIView
from Ausentismo.api.serializer import *
from datetime import date
from Ausentismo.api.APIs import get_data_api,get_data_api_Gestiones
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Case,When,CharField
from Ausentismo.api.email import enviar_correo_asesor,enviar_correo_lider
from collections import defaultdict
from django.db.models import Count

class Tiqueteradata(APIView):
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
        tipo_gestion = "Tiquetera"
        try:
            datos_api = get_data_api(cedula)
            Gestion_vacaciones_api = get_data_api_Gestiones(cedula,tipo_gestion) 
            if not datos_api:
                return JsonResponse({"message":"No se pudo encontrar el usuario"}, status=404)
            nombre = datos_api.get('Nombre')
            correo = request.data.get('correo')
            campana = datos_api.get('Campaña')
            cargo = datos_api.get('Cargo')
            fecha_peticion = date.today()
            tipo = request.data.get('tipo')
            estado = request.data.get('estado')
            beneficios = request.data.get('beneficio')
            Jefe_id = request.data.get('jefe')
            jefe = User.objects.get(id=Jefe_id)
            data = Tiquetera(
                    cedula = cedula,
                    nombre = nombre,
                    correo = correo,
                    fecha_peticion = fecha_peticion,
                    campana = campana,
                    cargo = cargo,
                    tipo = tipo,
                    estado = estado,
                    beneficios = beneficios,
                    Jefe_id = jefe
                )
            data.save()
            # Enviar correo
            subject = "<h1>Hola</h1>"
            body = "<h2>Hola su solicitud ha sido enviada y sera respondida prontamente</h2><br><p><strong>No responder</strong></p>"
            to_email = [correo]
            enviar_correo_asesor(subject,body,to_email)
            # Envio del correo al lider
            subject_lider = "<h1>Hola</h1>"
            body_lider = f"<h2>Se ha recibido la siguiente solicitud de tiquetera de {nombre}</h2><br>\
            <p><strong>Codigo Tiquetera:</strong> {data.codigo_tiquetera}</p><br>\
            <p><strong>Nombre completo:</strong> {nombre}</p><br>\
            <p><strong>Numero de identificacion:</strong> {cedula}</p><br>\
            <p><strong>Correo:</strong> {correo}</p><br>\
            <p><strong>Campaña:</strong> {campana}</p><br>\
            <p><strong>Cargo:</strong> {cargo}</p><br>\
            <p><strong>Jefe inmediato:</strong> {jefe.first_name}</p><br>\
            <p><strong>Sede:</strong> {tipo}</p><br>\
            <button>Aceptar</button>"
            to_email_lider = [jefe.email]
            enviar_correo_lider(subject_lider,body_lider,to_email_lider)
            # Serialize the last added record
            ultimo_usuario = Tiquetera.objects.last()
            serializer_usuario = Tiqueteraserializar(ultimo_usuario)
            return JsonResponse({'data': serializer_usuario.data, 'message': 'Datos agregados correctamente', "status": 200})
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({"message": f"Error processing request: {str(e)}"}, status=500)
        
    def put(self,request,id):
        tiqueteras = get_object_or_404(Tiquetera,id=id)
        tiqueteras.estado = request.data.get("estado")
        tiqueteras.observaciones = request.data.get("observaciones")
        tiqueteras.save()
        return JsonResponse({"message": "Registro actualizado con exito", "status":200})    

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

def filtrar_campañas_tiquerera(request,id):
    try:
        jefe = User.objects.get(id=id)
    except User.DoesNotExist:
        return JsonResponse({'error': 'Jefe no encontrado',"status":400}, status=404)
    permisos_relacionados = Tiquetera.objects.filter(Jefe_id=jefe).annotate(permisos_pendientes=Case(When(estado="Pendiente",then=0),default=1,output_field=CharField(),)).order_by('permisos_pendientes')
    permisos_list = list(permisos_relacionados.values())
    return JsonResponse({"data":permisos_list,"status":200},status = 200)

def obtener_estados_tiquetera(request):
    permisos_a_contar = ['Negado', 'Aceptado']
    
    permisos = Tiquetera.objects.filter(estado__in=permisos_a_contar).values('estado').annotate(count=Count('id'))
    
    permisos_count = defaultdict(int)
    
    for permiso in permisos:
        permisos_count[permiso['estado']] = permiso['count']
    
    permisos_negados = {'Negado': permisos_count['Negado']} if 'Negado' in permisos_count else {}
    permisos_aceptados = {'Aceptado': permisos_count['Aceptado']} if 'Aceptado' in permisos_count else {}
    
    return JsonResponse({
        'permisos negados': permisos_negados,
        'permisos aceptados': permisos_aceptados,
        'total permisos': sum(permisos_count.values())
    }, status=200)