from Ausentismo.api.serializer import *
import pandas as pd
import io
from django.http import HttpResponse
from datetime import date
import datetime
from django.utils.timezone import now

# Obtener el día de hoy
hoy = now().date()
def Exporte_permisos_quincenal(self):
        datos = []
        permisos = Permisos.objects.all()
        fecha = date.today()
        for permiso in permisos:
            if permiso.fecha_peticion ==  fecha:
                datos.append({
                    'Codigo Permiso': permiso.codigo_permiso,
                    'Cedula':permiso.cedula,
                    'Nombre':permiso.nombre,
                    'Campaña':permiso.campana,
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
def Exporte_permisos_semanal(self):
        datos = []
        permisos = Permisos.objects.all()
        fecha = date.today()
        inicio_semana  = datetime.timedelta(fecha.weekday())
        fin_semana = inicio_semana + datetime.timedelta(days=6)
        for permiso in permisos:
            if permiso.fecha_peticion in range(inicio_semana,fin_semana):
                datos.append({
                    'Codigo Permiso': permiso.codigo_permiso,
                    'Cedula':permiso.cedula,
                    'Nombre':permiso.nombre,
                    'Campaña':permiso.campana,
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
def Exporte_permisos_mensual(self):
        datos = []
        permisos = Permisos.objects.all()
        fecha_actual = date.today()
        mes_actual = fecha_actual.month
        print(f"mes:{mes_actual}")
        for permiso in permisos:
            print(permiso.fecha_peticion.month)
            if permiso.fecha_peticion.month == mes_actual:
                    datos.append({
                        'Codigo Permiso': permiso.codigo_permiso,
                        'Cedula':permiso.cedula,
                        'Nombre':permiso.nombre,
                        'Campaña':permiso.campana,
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
def Exporte_permisos_anual(self):
        datos = []
        fecha  = date.today()
        anio = fecha.year
        permisos = Permisos.objects.all()
        for permiso in permisos:
            if permiso.fecha_peticion.year == anio:
                datos.append({
                    'Codigo Permiso': permiso.codigo_permiso,
                    'Cedula':permiso.cedula,
                    'Nombre':permiso.nombre,
                    'Campaña':permiso.campana,
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
                "Campaña":solicitud.campana,
                "Cargo":solicitud.cargo,
                "Fecha inicio vacaciones":solicitud.fecha_inicio,
                "Fecha fin vacaciones":solicitud.fecha_incorporacion,
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
                "Campaña":solicitud.campana,
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
    
    
    