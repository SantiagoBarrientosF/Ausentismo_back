from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.     

class Vacaciones(models.Model):  
    Codigo_vacacione = models.CharField(unique=True,blank=True)  
    cedula = models.CharField(max_length=30,null=True)
    nombre = models.CharField (max_length=100,null=True)   
    correo = models.CharField (max_length=100,null=True)   
    fecha_ingreso_empresa = models.DateField(default=timezone.now)
    dias_vacaciones = models.CharField(max_length= 5)
    campana = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    fecha_peticion = models.DateField(default=timezone.now)
    fecha_inicio = models.DateField()
    fecha_incorporacion = models.DateField(default=timezone.now)
    observaciones = models.CharField(max_length=80)
    Jefe_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True,default=None)
    periodo = models.CharField(max_length=80)
    estado = models.CharField(max_length=80,default="Pendiente")
    
    def __str__(self,request):
        return f"{self.Codigo_vacacione}"
    def save(self, *args, **kwargs):
        if not self.Codigo_vacacione:  
            last_vacaciones = Vacaciones.objects.all().order_by('id').last()
            if last_vacaciones:
                last_codigo = last_vacaciones.Codigo_vacacione
                last_number = int(last_codigo.split('-')[1])
                new_number = last_number + 1
            else:
                new_number = 1  

            self.Codigo_vacacione = f"Vac-{new_number:06d}" 

        super(Vacaciones, self).save(*args, **kwargs)  
        
class beneficios_tiquetera(models.Model):
    beneficio = models.CharField(max_length=100)
    horas_disponibles = models.CharField(max_length=80)
    tipo = models.CharField(max_length=100,null=True)
    
class Tiquetera(models.Model):    
    cedula = models.CharField(max_length=100,null=True)
    codigo_tiquetera = models.CharField(max_length=100,unique=True,blank=True)
    nombre = models.CharField(max_length=100,null=True)
    campana = models.CharField(max_length=100,null=True)    
    cargo = models.CharField(max_length=100,null=True)    
    Jefe_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True,default=None)
    estado = models.CharField(max_length=100,null=True)
    beneficios = models.CharField(max_length=100, null = True)
    observaciones = models.CharField(max_length=100, default="Hola")
    correo = models.CharField(max_length=100,null=True)
    tipo = models.CharField(max_length=100,null=True)
    fecha_peticion = models.DateField(default=timezone.now)


    def __str__(self,request):
        return f"{self.codigo_tiquetera}"
    def save(self, *args, **kwargs):
        if not self.codigo_tiquetera:
            last_tiquetera = Tiquetera.objects.all().order_by('id').last()
            
            if last_tiquetera:
                last_codigo = last_tiquetera.codigo_tiquetera
                
                
                try:
                    last_number_Admin = int(last_codigo.split('-')[-1])
                    last_number_Rionegro = int(last_codigo.split('-')[-1])
                    last_number_Medellin = int(last_codigo.split('-')[-1])
                except ValueError:
                    last_number_Admin = 0  
                    last_number_Rionegro = 0  
                    last_number_Medellin = 0  
                
                new_number_admin = last_number_Admin + 1
                new_number_Rionegro_Ceja = last_number_Rionegro + 1
                new_number_Medellin_Bogota = last_number_Medellin + 1
            else:
                new_number_admin = 1
                new_number_Rionegro_Ceja =  1
                new_number_Medellin_Bogota =  1
    
            
            if self.tipo == "Medellin/Bogota":
                self.codigo_tiquetera = f"Tiq_Med-Bog-{new_number_Medellin_Bogota:06d}" 
            elif self.tipo == "Rionegro/La Ceja":
                self.codigo_tiquetera = f"Tiq_Ceja-Rio-{new_number_Rionegro_Ceja:06d}"
            elif self.tipo == "Administrativos":
                self.codigo_tiquetera = f"Tiq_Adm-{new_number_admin:06d}"
    
        super(Tiquetera, self).save(*args, **kwargs)

class Permisos(models.Model):
    codigo_permiso = models.CharField(unique=True,blank=True,null=True)
    cedula = models.CharField(max_length=30,null=True)
    nombre = models.CharField (max_length=100,null=True)   
    correo = models.CharField (max_length=100,null=True)   
    fecha_ingreso_empresa = models.DateField(default=timezone.now)
    campana = models.CharField(max_length=100,null=True)
    cargo = models.CharField(max_length=100,null=True)
    fecha_peticion = models.DateField(default=timezone.now)
    fecha_inicio = models.DateField(default=timezone.now)
    fecha_incorporacion = models.DateField(default=timezone.now)
    Jefe_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True,default=0)
    observaciones = models.CharField(max_length=80)
    tipo_permiso = models.CharField(max_length=80,null=True)
    parentesco = models.CharField(max_length=100,null=True)
    estado = models.CharField(max_length=100,default="Pendiente")
    
    def __str__(self,request):
        return f"{self.codigo_permiso}"
    def save(self, *args, **kwargs):
        if not self.codigo_permiso:  
            last_permiso = Permisos.objects.all().order_by('id').last()
            if last_permiso:
                last_codigo = last_permiso.codigo_permiso
                last_number = int(last_codigo.split('-')[1])
                new_number = last_number + 1
            else:
                new_number = 1  

            self.codigo_permiso = f"Per-{new_number:06d}" 

        super(Permisos, self).save(*args, **kwargs)
    
class Incapacidades(models.Model):    
    cedula = models.CharField(max_length=30,null=True)
    nombre = models.CharField (max_length=100,null=True)   
    campana = models.CharField(max_length=100,null=True)
    cargo = models.CharField(max_length=100,null=True)
    turno = models.CharField(max_length=100)
    sede = models.CharField(max_length=100)
    doc_incapacidad =models.FileField(upload_to='incapacidades/', blank=True, null=True)
    lider = models.ForeignKey(User,on_delete=models.CASCADE,null=True,default=None)
    fecha_inicio = models.DateField(default=timezone.now)
    fecha_incorporacion = models.DateField(default=timezone.now)
    fecha_peticion = models.DateField(default=timezone.now)
    radicado = models.CharField(max_length=100,null=True)
    estado = models.CharField(max_length=100,default="Pendiente")


    
