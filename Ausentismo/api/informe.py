from Ausentismo.api.serializer import *
import pandas as pd
import io
from django.http import HttpResponse
from datetime import datetime
from rest_framework.views import APIView
from django.http import JsonResponse

class Exporte_gestiones(APIView):        
    def Exporte_permisos(self,id,fecha_inicio,fecha_fin):
            datos = []
            permisos = Permisos.objects.filter(Jefe_id = id, 
            fecha_peticion__gte=fecha_inicio,
            fecha_peticion__lte=fecha_fin).order_by("codigo_permiso")
            for permiso in permisos:
                datos.append({
                    'Codigo Permiso': permiso.codigo_permiso,
                    'Cedula':permiso.cedula,
                    'Nombre':permiso.nombre,
                    'Campaña':permiso.campana,
                    'Cargo':permiso.cargo,
                    'Fecha inicio permiso':permiso.fecha_inicio,
                    'Fecha fin permiso':permiso.fecha_incorporacion,
                    'Tipo permiso':permiso.tipo_permiso,
                })
            return datos
        
    def get(self, request,*args, **kwargs):
        id  = self.kwargs.get('id')
        fecha_inicio = self.kwargs.get('fecha_inicio')
        fecha_fin = self.kwargs.get('fecha_fin')
        tipo_permiso = self.kwargs.get('tipo_permiso')
        # Cambiar formato de la fecha
        try:
            fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d').date()
            fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d').date()
            if tipo_permiso == "permiso":
                datos = self.Exporte_permisos(id,fecha_inicio, fecha_fin)
            elif tipo_permiso == "vacaciones":
                datos = self.Exporte_vacaciones(id,fecha_inicio, fecha_fin)    
            elif tipo_permiso == "tiquetera":
                datos = self.Exporte_Tiquetera(id,fecha_inicio, fecha_fin)     
            elif tipo_permiso == "General":
                datos = self.Exporte_general(id,fecha_inicio, fecha_fin)     
            df = pd.DataFrame(datos)
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df.to_excel(writer, index=False)
            response = HttpResponse(output.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = f'attachment; filename=Informe_{tipo_permiso}_{fecha_inicio}_{fecha_fin}.xlsx'
            return response
        except Exception as e:
            return JsonResponse({"message":f"No se puede descargar el archivo: {e}"},status = 500)
    def Exporte_vacaciones(self,id,fecha_inicio,fecha_fin):
        datos = []
        vacaciones = Vacaciones.objects.filter(Jefe_id =id,
        fecha_peticion__gte=fecha_inicio,
        fecha_peticion__lte=fecha_fin).order_by("Codigo_vacacione")
        for solicitud in vacaciones:
            datos.append({
                "Codigo Vacacaciones":solicitud.Codigo_vacacione,
                "Cedula":solicitud.cedula,
                "Nombre":solicitud.nombre,
                "Campaña":solicitud.campana,
                "Cargo":solicitud.cargo,
                "Fecha inicio vacaciones":solicitud.fecha_inicio,
                "Fecha fin vacaciones":solicitud.fecha_incorporacion,
                "Periodo":solicitud.periodo,
            })
        return datos
    
    def Exporte_Tiquetera(self,id,fecha_inicio,fecha_fin):
        datos = []
        tiquetera = Tiquetera.objects.filter(Jefe_id = id,
        fecha_peticion__gte=fecha_inicio,
        fecha_peticion__lte=fecha_fin).order_by("codigo_tiquetera")
        for solicitud in tiquetera:
            datos.append({
                "Codigo Tiquetera":solicitud.codigo_tiquetera,
                "Cedula":solicitud.cedula,
                "Nombre":solicitud.nombre,
                "Campaña":solicitud.campana,
                "Beneficios":solicitud.beneficios,
                "Tipo":solicitud.tipo,
                "Estado":solicitud.estado,
                "Fecha peticion": solicitud.fecha_peticion
            })
        return datos
def Exporte_general(self,id,fecha_inicio,fecha_fin):
    datos = []
    vacaciones = Vacaciones.objects.filter(Jefe_id =id,
    fecha_peticion__gte=fecha_inicio,
    fecha_peticion__lte=fecha_fin).order_by("Codigo_vacacione")
    for solicitud in vacaciones:
        datos.append({
            "Codigo Vacacaciones":solicitud.Codigo_vacacione,
            "Cedula":solicitud.cedula,
            "Nombre":solicitud.nombre,
            "Campaña":solicitud.campana,
            "Cargo":solicitud.cargo,
            "Fecha inicio vacaciones":solicitud.fecha_inicio,
            "Fecha fin vacaciones":solicitud.fecha_incorporacion,
            "Periodo":solicitud.periodo,
        })
    return datos