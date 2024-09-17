from rest_framework import serializers
from django.contrib.auth.models import User
from Ausentismo.models import *
# from Ausentismo.models import Agentes, Conexion,Licencias,Factura

# The `UserSerializer` class defines a serializer for the User model with specified fields.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
 
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id','Nombre', 'Username','Apellido']        