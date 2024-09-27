from django.db import models
from django.utils import timezone


# Create your models here.     
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
    observaciones = models.CharField(max_length=80)
    jefe = models.CharField(max_length=80)
class Tiquetera(models.Model):    
    cedula = models.CharField(max_length=100)
    codigo_tiquetera = models.CharField(max_length=100,unique=True,blank=True)
    nombre = models.CharField(max_length=100)
    campaña = models.CharField(max_length=100)    
    jefe = models.CharField(max_length=100)
    fecha_peticion = models.DateField()
    estado = models.CharField(max_length=100)
    beneficios = models.CharField(max_length=100)
    sede = models.CharField(max_length=100)
    tipo_tiquetera = models.CharField()
    def __str__(self,request):
        return f"{self.codigo_tiquetera}"
    def save(self, *args, **kwargs):
        if not self.codigo_tiquetera:  
            last_tiquetera = Tiquetera.objects.all().order_by('id').last()
            if last_tiquetera and self.tipo_tiquetera == "emocional":
                last_codigo = last_tiquetera.codigo_tiquetera
                last_number = int(last_codigo.split('-')[1])
                new_number = last_number + 1
            else:
                new_number = 1  
        
            self.codigo_tiquetera = f"Tiq_emoc-{new_number:06d}" 
            
        if last_tiquetera and self.tipo_tiquetera == "personal":
                last_codigo = last_tiquetera.codigo_tiquetera
                last_number = int(last_codigo.split('-')[1])
                new_number = last_number + 1
        else:
                new_number = 1  
        
        self.codigo_tiquetera = f"Tiq_pers-{new_number:06d}" 
        
        super(Tiquetera, self).save(*args, **kwargs)
class Permisos(models.Model):
    codigo_permiso = models.CharField(unique=True,blank=True,null=True)
    cedula = models.CharField(max_length=30)
    nombre = models.CharField (max_length=100)   
    correo = models.CharField (max_length=100)   
    fecha_ingreso_empresa = models.DateField(timezone.now())
    campaña = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    fecha_peticion = models.DateField(timezone.now())
    fecha_inicio = models.DateField(default=timezone.now())
    fecha_fin = models.DateField(default=timezone.now())
    fecha_incorporacion = models.DateField(timezone.now())
    jefe = models.CharField(max_length=80)
    tipo_permiso = models.CharField(max_length=80)
    parentesco = models.CharField(max_length=100,null=True)
    
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

    
class Historial_permisos(models.Model):
    id_permisos = models.ForeignKey(Permisos,on_delete=models.CASCADE,null = True)
    fecha = models.DateTimeField(timezone.now())
    Estados  = models.CharField(max_length=100)
