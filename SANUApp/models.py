
from django.db import models

# Create your models here.
class Integrente(models.Model):
    Nombre_Integrante = models.CharField(max_length=100, verbose_name='Nombre de Integrante')
    Descripcion = models.TextField(max_length=800, verbose_name='Descripcion del integrante')
    FotoIntegrante = models.ImageField(upload_to="Integrantes")
    
    def __str__(self):
        descripcion = self.Nombre_Integrante
        return descripcion
    
    def delete(self, using=None, keep_parents=False):
        self.FotoIntegrante.storage.delete(self.FotoIntegrante.name)
        super().delete()
        
class Servicios(models.Model):
    Nombre_Servicio = models.CharField(max_length=120, verbose_name="Servicio")
    Descripcion_Servicio = models.TextField(max_length=500, verbose_name="Descripcion")
    Foto_Servicio = models.ImageField(upload_to="Servicios")

    def __str__(self):
        descripcion = self.Nombre_Servicio
        return descripcion
    
    def delete(self, using=None, keep_parents=False):
        self.Foto_Servicio.storage.delete(self.Foto_Servicio.name)
        super().delete()
class Comentarios(models.Model):
    Nombre_Paciente = models.CharField(max_length=120, verbose_name="Nombre del paciente")
    Descripcion_Comentario = models.TextField(max_length=1000, verbose_name="Descripcion del servicio brindado y atencion")
    Calificacion = models.IntegerField(verbose_name="¡Califica nuestro servicio de 1 a 5 Estrellas!")
    Foto_Paciente = models.ImageField()
    Fecha_Comentario = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        descripcion = self.Nombre_Paciente
        return descripcion
    
    def delete(self, using=None, keep_parents=False):
        self.Foto_Paciente.storage.delete(self.Foto_Paciente.name)
        super().delete()
