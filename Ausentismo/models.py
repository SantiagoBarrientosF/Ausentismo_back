from django.db import models
from django.utils import timezone


# Create your models here.

class Usuario(models.Model):
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100,default=" ")
    Rol = models.CharField(max_length=100)
    Sede = models.CharField(max_length=100)
    Cargo = models.CharField(max_length=100)
    Username = models.CharField(max_length=100)
    Password  = models.CharField(max_length=100)       
     
class Vacaciones(models.Model):  
    Codigo_vacacione = models.CharField(unique=True,blank=True)  
    cedula = models.CharField(max_length=30)
    nombre = models.CharField (max_length=100)   
    correo = models.CharField (max_length=100)   
    fecha_ingreso_empresa = models.DateField(timezone.now())
    dias_vacaciones = models.CharField(max_length= 5)
    campaña = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    fecha_inicio = models.DateField(timezone.now())
    fecha_fin = models.DateField()
    fecha_incorporacion = models.DateField(timezone.now())
    observaciones = models.CharField(max_length=80)
    jefe = models.CharField(max_length=80)
   
    
  
class Tiquetera(models.Model):    
    motivo = models.CharField(max_length=200)
    fecha_inicio = models.DateField(timezone.now())
    fecha_fin = models.DateField(timezone.now())
    tipo_tiquetera = models.CharField(max_length=100)
    sede  = models.CharField(max_length=100)
    estado = models.CharField(max_length=80)
    
class Permisos(models.Model):
    codigo_permiso = models.CharField(unique=True,blank=True)
    cedula = models.CharField(max_length=30)
    nombre = models.CharField (max_length=100)   
    correo = models.CharField (max_length=100)   
    fecha_ingreso_empresa = models.DateField(timezone.now())
    campaña = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    fecha_peticion = models.DateField(timezone.now())
    fecha_incorporacion = models.DateField(timezone.now())
    observaciones = models.CharField(max_length=80)
    jefe = models.CharField(max_length=80)
    tipo_permiso = models.CharField(max_length=80)
    parentesco = models.CharField(max_length=100,null=True)
    
class Historial(models.Model):
    id_vacaciones = models.ForeignKey(Vacaciones,on_delete=models.CASCADE,null = True)
    id_permisos = models.ForeignKey(Permisos,on_delete=models.CASCADE,null = True)
    id_tiquetera = models.ForeignKey(Tiquetera,on_delete=models.CASCADE,null = True)
    fecha = models.DateTimeField(timezone.now())

