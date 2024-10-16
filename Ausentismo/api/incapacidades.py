from Ausentismo.models import *
from Ausentismo.api.serializer import *
from django.http import JsonResponse,HttpResponse
from rest_framework.views import APIView
from django.http import JsonResponse 
from django.http import HttpResponse
import pandas as pd
import io
from collections import defaultdict,Counter

class Incapacidadesdata(APIView):
#  authentication_classes = [TokenAuthentication]
#  permission_classes = [IsAuthenticated]
   def get(self,request):    
      Valor= Permisos.objects.filter(tipo_permiso__in=["Licencia remunerada","Licencia no remunerada"]) 
      items_list = []
      for item in Valor: 
         item_dict = {
            'Nombre':item.nombre,
            'Cargo':item.cargo, 
            'Campaña':item.campaña, 
            'Fecha_ingreso_empresa':item.fecha_ingreso_empresa, 
            'Fecha_permiso':item.fecha_peticion, 
         }
         items_list.append(item_dict)
      return JsonResponse(items_list, safe=False) 


def export_incapacidades(self):
   incapacidades = Permisos.objects.filter(tipo_permiso__in=["Licencia remunerada","Licencia no remunerada"])
   datos = []
   
   for solicitud in incapacidades:
      datos.append({
         "Cedula": solicitud.cedula,
         "Nombre": solicitud.nombre,
         "Cargo": solicitud.cargo,
         "Campaña": solicitud.campaña,
         "Fecha inicio incapacidad": solicitud.fecha_inicio,
         "Fecha fin incapacidad": solicitud.fecha_fin,
         "Tipo_permiso": solicitud.tipo_permiso,
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
         incapacidad_por_campaña[incapacidad.campaña][incapacidad.nombre] += 1
      return JsonResponse(dict(incapacidad_por_campaña),safe=False)
   
def Contarincapacidades_campaña(self):
      incapacidades = Permisos.objects.filter(tipo_permiso__in=["Licencia remunerada", "Licencia no remunerada"])
      incapacidad_por_campaña = defaultdict(Counter)
      for incapacidad in incapacidades:
         incapacidad_por_campaña[incapacidad.campaña][incapacidad.campaña]+= 1
      return JsonResponse(dict(incapacidad_por_campaña),safe=False)
