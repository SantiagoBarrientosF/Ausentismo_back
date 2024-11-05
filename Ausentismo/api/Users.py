from Ausentismo.models import *
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from Ausentismo.api.serializer import *
from django.shortcuts import get_object_or_404

class Usersdata(APIView):
   # authentication_classes = [TokenAuthentication]
   # permission_classes = [IsAuthenticated]
   def get(self,request):    
      Valor= User.objects.filter(is_staff=True) 
      items_list = []
      for item in Valor: 
         item_dict = {
            'id': item.id,
            'Nombre':item.first_name,
            'Staff':item.is_staff, 
         }
         items_list.append(item_dict)
      return JsonResponse(items_list, safe=False) 
   
   def post(self,request):
      if request.method == 'POST':
         first_name = request.data.get('nombre')
         email = request.data.get('correo')
         username = request.data.get('username')
         password = request.data.get('password')
         is_staff = request.data.get('staff')
         print(request.data)
      if first_name and email and username  and password and is_staff:
         data  = User(
               first_name = first_name,
               email = email,
               username = username,
               password = password,
               is_staff = is_staff,
         )
         data.save()
         ultimo_usuario = User.objects.last()
         serializer_usuario = UserSerializer(ultimo_usuario)
         return JsonResponse({'data': serializer_usuario.data, 'message': 'Datos agregados correctamente'})

class update_conceptos(APIView):
      def put(self,request,id):
         users = get_object_or_404(User,id=id) 
         users.Nombre = request.data.get('nombre')
         users.Apellido = request.data.get('apellido')
         users.Username = request.data.get('username')
         users.Rol = request.data.get('rol')
         users.Sede = request.data.get('sede')
         users.save()
         return JsonResponse({'data': 'Success', 'message': 'Datos actualizados correctamente'}) 


class usuarios(APIView):
  def get(self,request):    
      Valor= User.objects.all()
      items_list = []
      for item in Valor: 
         item_dict = {
            'id':item.id,
            'Username': item.username,
            'First_name':item.first_name,
            'Rol':item.groups.name,
            'Last_name':item.last_name,
            'Email':item.email, 
         }
         items_list.append(item_dict)
      return JsonResponse({"data":items_list}, safe=False)
   