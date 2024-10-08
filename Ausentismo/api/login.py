from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializer import UserSerializer
from django.contrib.auth.models import User
from rest_framework import  status 
from Ausentismo.models import *
from django.shortcuts import  get_object_or_404 
from django.views.decorators.csrf import csrf_exempt
from Ausentismo.api.signals import *

@api_view(['POST']) 
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    grupos = user.groups.all()
    if not user.check_password(request.data['password']):
        return Response({"error": "Credenciales incorrectas"}, status=status.HTTP_400_BAD_REQUEST)  
    token, created = Token.objects.get_or_create(user = user)   
    serializer = UserSerializer(instance=user)
    for grupo in grupos:
     roles = {
        "rol":grupo.name
     }
    return Response({'token': token.key ,'user': serializer.data, 'roles':roles},status=status.HTTP_201_CREATED)

@csrf_exempt
@api_view(['POST'])
def logout(request):
    user = get_object_or_404(User, auth_token=request.data['Token'])
    print(user)
    if not getattr(user, "is_authenticated", True):
        user = None
    user_logged_out.send(sender=user.__class__, request=request, user=user)
    request.session.flush()
    if hasattr(request, "user"):
        from django.contrib.auth.models import AnonymousUser
        request.user = AnonymousUser()
        return  Response("Sesión cerrada con exíto",status=status.HTTP_200_OK) 

@api_view(['POST']) 
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        Usuario = serializer.save()   
        Usuario = User.objects.get(username=serializer.data['username'])
        Usuario.set_password(request.data['password'])
        Usuario.save()
        token = Token.objects.create(user = Usuario)
        return Response({'token': token.key,'user': serializer.data},status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

    