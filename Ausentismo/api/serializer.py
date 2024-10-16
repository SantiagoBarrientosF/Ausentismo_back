from rest_framework import serializers
from django.contrib.auth.models import User
from Ausentismo.models import *

# The `UserSerializer` class defines a serializer for the User model with specified fields.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name','is_staff','is_superuser']
 
class Tiqueteraserializar(serializers.ModelSerializer):
    class Meta:
        model = Tiquetera
        fields = '__all__'

class Vacacioneserializar(serializers.ModelSerializer):
    class Meta:
        model = Vacaciones
        fields = '__all__'
        
class Permisoserializar(serializers.ModelSerializer):
    class Meta:
        model = Permisos
        fields = '__all__'                

class Historialserializar(serializers.ModelSerializer):
    class Meta:
        model = Historial_permisos
        fields = '__all__'                              