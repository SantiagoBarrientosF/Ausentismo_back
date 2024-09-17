from django.db import models
from django.utils import timezone


# Create your models here.
# class Informe(models.Model):
#    Nombre = models.CharField(max_length=100)
#    Rol = models.CharField(max_length=100)
#    Sede = models.CharField(max_length=100)
#    Cargo = models.CharField(max_length=100)
    
class Usuario(models.Model):
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100,default=" ")
    Rol = models.CharField(max_length=100)
    Sede = models.CharField(max_length=100)
    Cargo = models.CharField(max_length=100)
    Username = models.CharField(max_length=100)
    Password  = models.CharField(max_length=100)   
     
# class Vacaciones(models.Model):    
#     fecha_inicio = models.CharField(max_length=200)
#     fecha_fin = models.CharField(max_length=0)
#     id_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,null = True) 
  
class Permisos(models.Model):    
    motivo = models.CharField(max_length=200)
    fecha_inicio = models.CharField(max_length=200)
    fecha_fin = models.IntegerField(default=0)
    tipo_permiso = models.CharField(max_length=100)
    estado = models.CharField(max_length=80)

class Historial(models.Model):
    id_proceso = models.ForeignKey(Usuario,on_delete=models.CASCADE,null = True)
    fecha = models.DateTimeField(timezone.now())

