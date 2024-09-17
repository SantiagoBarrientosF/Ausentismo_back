from django.db import models
from django.utils import timezone


# Create your models here.
# class Informe(models.Model):
#    Nombre = models.CharField(max_length=100)
#    Rol = models.CharField(max_length=100)
#    Sede = models.CharField(max_length=100)
#    Cargo = models.CharField(max_length=100)
    
     
class Vacaciones(models.Model):    
    fecha_inicio = models.DateTimeField(timezone.now())
    fecha_fin = models.DateTimeField(timezone.now())
    
  
class Tiquetera(models.Model):    
    motivo = models.CharField(max_length=200)
    fecha_inicio = models.DateTimeField(timezone.now())
    fecha_fin = models.DateTimeField(timezone.now())
    tipo_tiquetera = models.CharField(max_length=100)
    sede  = models.CharField(max_length=100)
    estado = models.CharField(max_length=80)
    
class Permisos(models.Model):
    cedula = models.CharField(max_length=30)
    nombre = models.CharField (max_length=100)   
    correo = models.CharField (max_length=100)   
    fecha_ingreso_empresa = models.DateTimeField(timezone.now())
    fecha_inicio = models.DateTimeField(timezone.now())
    campaña = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    fecha_inicio = models.DateTimeField(timezone.now())
    fecha_fin = models.DateTimeField(timezone.now())
    fecha_incorporacion = models.DateTimeField(timezone.now())
    observaciones = models.CharField(max_length=80)
    jefe = models.CharField(max_length=80)
    tipo_permiso = models.CharField(max_length=80)
    
class Historial(models.Model):
    # id_proceso = models.ForeignKey(Usuario,on_delete=models.CASCADE,null = True)
    fecha = models.DateTimeField(timezone.now())

