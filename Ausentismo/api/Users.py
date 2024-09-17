from Ausentismo.models import *
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from Ausentismo.api.serializer import *

class Usersdata(APIView):
#    authentication_classes = [TokenAuthentication]
#    permission_classes = [IsAuthenticated]
   def get(self,request):    
      Valor= Usuario.objects.all() 
      Valores_list = list(Valor.values())
      return JsonResponse(Valores_list, safe=False) 
  
   def post(self,request):
      if request.method == 'POST':
         Nombre = request.data.get('nombre')
         Apellido = request.data.get('apellido')
         Username = request.data.get('username')
         Rol = request.data.get('rol')
         Sede = request.data.get('sede')
         Password = request.data.get('password')
         print(request.data)
      if Nombre and Apellido and Username and Rol and Sede and Password:
          data  = Usuario(
               Nombre = Nombre,
               Apellido = Apellido,
               Username = Username,
               Rol = Rol,
               Sede = Sede,
               Password = Password,
            )
          data.save()
          ultimo_concepto = Usuario.objects.last()
          serializer_concepto = UsuarioSerializer(ultimo_concepto)
          return JsonResponse({'data': serializer_concepto.data, 'message': 'Datos agregados correctamente'})





