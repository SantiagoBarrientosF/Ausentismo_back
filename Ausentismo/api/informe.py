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
            if id == 2:
                permisos = Permisos.objects.all().filter(fecha_peticion__gte=fecha_inicio,
            fecha_peticion__lte=fecha_fin).order_by("codigo_permiso")
            else:    
               permisos = Permisos.objects.filter(Jefe_id = id, 
               fecha_peticion__gte=fecha_inicio,
               fecha_peticion__lte=fecha_fin).order_by("codigo_permiso")
            for solicitudes in permisos:
                datos.append({
                    'Codigo Permiso': solicitudes.codigo_permiso,
                    'Cedula':solicitudes.cedula,
                    'Nombre':solicitudes.nombre,
                    'Campaña':solicitudes.campana,
                    'Cargo':solicitudes.cargo,
                    'Fecha inicio permiso':solicitudes.fecha_inicio,
                    'Fecha fin permiso':solicitudes.fecha_incorporacion,
                    'Tipo permiso':solicitudes.tipo_permiso,
                })
            return datos
    def get(self, request,*args, **kwargs):
        id  = self.kwargs.get('id')
        fecha_inicio = self.kwargs.get('fecha_inicio')
        fecha_fin = self.kwargs.get('fecha_fin')
        tipo_permiso = self.kwargs.get('tipo_permiso')
        # Cambiar formato de la fecha
        try:
            if tipo_permiso == "General":
                datos_vacaciones,datos_permisos,datos_tiquetera,datos_incapacidades = self.Exporte_general(id,fecha_inicio, fecha_fin)
                df_vacaciones = pd.DataFrame(datos_vacaciones)
                df_permisos = pd.DataFrame(datos_permisos)
                df_tiquetera = pd.DataFrame(datos_tiquetera)
                df_incapacidades = pd.DataFrame(datos_incapacidades)
                # Crear archivo Excel con varias hojas  
                output = io.BytesIO()
                with pd.ExcelWriter(output, engine='openpyxl') as writer:
                    df_vacaciones.to_excel(writer, sheet_name='Vacaciones', index=False)
                    df_permisos.to_excel(writer, sheet_name='Permisos', index=False)
                    df_tiquetera.to_excel(writer, sheet_name='Tiquetera', index=False)
                    df_incapacidades.to_excel(writer, sheet_name='Incapacidades', index=False)
                output.seek(0)
                response = HttpResponse(output.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                response['Content-Disposition'] = f'attachment; filename=Informe_General_{fecha_inicio}_{fecha_fin}.xlsx'
                return response
            elif tipo_permiso == "Permisos":
                datos = self.Exporte_permisos(id,fecha_inicio, fecha_fin)
            elif tipo_permiso == "Vacaciones":
                datos = self.Exporte_vacaciones(id,fecha_inicio, fecha_fin)    
            elif tipo_permiso == "Tiquetera":
                datos = self.Exporte_Tiquetera(id,fecha_inicio, fecha_fin)     
            elif tipo_permiso == "Incapacidades":
                datos = self.Exporte_incapacidades(id,fecha_inicio, fecha_fin)
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
        if id == 2:
            vacaciones = Vacaciones.objects.all().filter(fecha_peticion__gte=fecha_inicio,
            fecha_peticion__lte=fecha_fin).order_by("Codigo_vacaciones")
        else:
            vacaciones = Vacaciones.objects.filter(Jefe_id =id,
            fecha_peticion__gte=fecha_inicio,
            fecha_peticion__lte=fecha_fin).order_by("Codigo_vacaciones")
        for solicitud in vacaciones:
            datos.append({
            "Codigo Vacacaciones":solicitud.Codigo_vacaciones,
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
        if id == 2:
            tiquetera = Tiquetera.objects.all().filter(fecha_peticion__gte=fecha_inicio,
            fecha_peticion__lte=fecha_fin).order_by("codigo_tiquetera")
        else:
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
        datos_vacaciones = []
        datos_permisos = []
        datos_tiquetera = []
        datos_incapacidades = []
        if id == 2:
            vacaciones = Vacaciones.objects.all().filter(fecha_peticion__gte=fecha_inicio,fecha_peticion__lte=fecha_fin).order_by("Codigo_vacaciones")
            permiso = Permisos.objects.all().filter(fecha_peticion__gte=fecha_inicio,fecha_peticion__lte=fecha_fin).order_by("codigo_permiso")
            tiquetera = Tiquetera.objects.all().filter(fecha_peticion__gte=fecha_inicio,fecha_peticion__lte=fecha_fin).order_by("codigo_tiquetera")
            incapacidades = Incapacidades.objects.all().filter(fecha_peticion__gte=fecha_inicio,fecha_peticion__lte=fecha_fin).order_by("radicado")
        else:
            vacaciones = Vacaciones.objects.filter(Jefe_id =id,
            fecha_peticion__gte=fecha_inicio,
            fecha_peticion__lte=fecha_fin).order_by("Codigo_vacaciones")
            permiso = Permisos.objects.filter(Jefe_id =id,
            fecha_peticion__gte=fecha_inicio,
            fecha_peticion__lte=fecha_fin).order_by("codigo_permiso")
            tiquetera = Tiquetera.objects.filter(Jefe_id =id,
            fecha_peticion__gte=fecha_inicio,
            fecha_peticion__lte=fecha_fin).order_by("codigo_tiquetera")
            incapacidades = Incapacidades.objects.filter(Jefe_id =id,
            fecha_peticion__gte=fecha_inicio,
            fecha_peticion__lte=fecha_fin).order_by("radicado")
        for solicitud_vacaciones in vacaciones:
            datos_vacaciones.append({
                "Codigo Vacacaciones": solicitud_vacaciones.Codigo_vacaciones,
                "Cedula": solicitud_vacaciones.cedula,
                "Nombre": solicitud_vacaciones.nombre,
                "Campaña": solicitud_vacaciones.campana,
                "Cargo": solicitud_vacaciones.cargo,
                "Fecha inicio vacaciones": solicitud_vacaciones.fecha_inicio,
                "Fecha fin vacaciones": solicitud_vacaciones.fecha_incorporacion,
                "Periodo": solicitud_vacaciones.periodo
            })

        for solicitud_permiso in permiso:
            datos_permisos.append({
                "Codigo Permiso": solicitud_permiso.codigo_permiso,
                "Cedula": solicitud_permiso.cedula,
                "Nombre": solicitud_permiso.nombre,
                "Campaña": solicitud_permiso.campana,
                "Cargo": solicitud_permiso.cargo,
                "Fecha inicio permiso": solicitud_permiso.fecha_inicio,
                "Fecha fin permiso": solicitud_permiso.fecha_incorporacion
            })

        for solicitud_tiquetera in tiquetera:
            datos_tiquetera.append({
                "Codigo Tiquetera": solicitud_tiquetera.codigo_tiquetera,
                "Cedula": solicitud_tiquetera.cedula,
                "Nombre": solicitud_tiquetera.nombre,
                "Campaña": solicitud_tiquetera.campana,
                "Cargo": solicitud_tiquetera.cargo,
                "Fecha peticion tiquetera": solicitud_tiquetera.fecha_peticion
            })
        for solicitud_incapacidades in incapacidades:
            datos_incapacidades.append({
                "Radicado incapacidad": solicitud_incapacidades.radicado,
                "Cedula": solicitud_incapacidades.cedula,
                "Nombre": solicitud_incapacidades.nombre,
                "Cargo": solicitud_incapacidades.cargo,
                "Campaña": solicitud_incapacidades.campana,
                "Fecha inicio incapacidad": solicitud_incapacidades.fecha_inicio_incapacidad,
                "Fecha termino incapacidad": solicitud_incapacidades.fecha_terminacion_incapacidad,
                "Fecha incorporacion": solicitud_incapacidades.fecha_incorporacion,
            })
        return datos_vacaciones,datos_permisos,datos_tiquetera,datos_incapacidades,datos_incapacidades
    def Exporte_incapacidades(self,id,fecha_inicio,fecha_fin):
        if id == 2:
            incapacidad = Incapacidades.objects.all()
        else:
            incapacidad = Incapacidades.objects.filter(lider_id = id,fecha_peticion__gte=fecha_inicio,
            fecha_peticion__lte=fecha_fin).order_by("id")
        datos = []
        for solicitud in incapacidad:
            datos.append({
               "Radicado incapacidad":solicitud.radicado,
               "Cedula": solicitud.cedula,
               "Nombre": solicitud.nombre,
               "Cargo": solicitud.cargo,
               "Campaña": solicitud.campana,
               "Fecha inicio incapacidad": solicitud.fecha_inicio_incapacidad,
               "Fecha termino incapacidad": solicitud.fecha_terminacion_incapacidad,
               "Fecha incorporacion": solicitud.fecha_incorporacion,
            })
        return datos
    

    