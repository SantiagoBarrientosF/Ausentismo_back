from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from Ausentismo.api.serializer import *
import pandas as pd
import io
from django.http import HttpResponse

def Exporte_permisos(self,request):
        datos = []
        permisos = Permisos.objects.all()
        for permiso in permisos:
            datos.append({
                'Codigo Permiso': permiso.codigo_permiso,
                'Cedula':permiso.cedula,
                'Nombre':permiso.nombre,
                'Campaña':permiso.campaña,
                'Cargo':permiso.cargo,
                'Fecha inicio permiso':permiso.fecha_inicio,
                'Fecha fin permiso':permiso.fecha_fin,
                'Tipo permiso':permiso.tipo_permiso,
            })
        df = pd.DataFrame(datos)
        output = io.BytesIO() 
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False)
        
        response = HttpResponse(output.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=Informe_permisos.xlsx'
        return response
def Exporte_vacaciones(self):
        datos = []
        vacaciones = Vacaciones.objects.all()
        for solicitud in vacaciones:
            datos.append({
                "Codigo Vacacaciones":solicitud.Codigo_vacacione,
                "Cedula":solicitud.cedula,
                "Nombre":solicitud.nombre,
                "Campaña":solicitud.campaña,
                "Cargo":solicitud.cargo,
                "Fecha inicio vacaciones":solicitud.fecha_inicio,
                "Fecha fin vacaciones":solicitud.fecha_fin,
                "Periodo":solicitud.periodo,
            })
        df  =pd.DataFrame(datos)
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False)
        response = HttpResponse(output.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=Informe_vacaciones.xlsx'
        return response
def Exporte_Tiquetera(self):
        datos = []
        tiquetera = Tiquetera.objects.all()
        for solicitud in tiquetera:
            datos.append({
                "Codigo Tiquetera":solicitud.codigo_tiquetera,
                "Cedula":solicitud.cedula,
                "Nombre":solicitud.nombre,
                "Campaña":solicitud.campaña,
                "Beneficios":solicitud.beneficios,
                "Tipo":solicitud.tipo,
                "Estado":solicitud.estado
            })
        df  =pd.DataFrame(datos)
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False)
        response = HttpResponse(output.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=Informe_Tiquetera.xlsx'
        return response