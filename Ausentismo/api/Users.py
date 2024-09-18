from Ausentismo.models import *
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from Ausentismo.api.serializer import *
from django.shortcuts import get_object_or_404

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
          ultimo_usuario = Usuario.objects.last()
          serializer_usuario = UsuarioSerializer(ultimo_usuario)
          return JsonResponse({'data': serializer_usuario.data, 'message': 'Datos agregados correctamente'})

class update_conceptos(APIView):
      def put(self,request,id):
         users = get_object_or_404(Usuario,id=id) 
         users.Nombre = request.data.get('nombre')
         users.Apellido = request.data.get('apellido')
         users.Username = request.data.get('username')
         users.Rol = request.data.get('rol')
         users.Sede = request.data.get('sede')
         users.save()
         return JsonResponse({'data': 'Success', 'message': 'Datos actualizados correctamente'}) 



