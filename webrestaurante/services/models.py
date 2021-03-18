from django.db import models

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=200,  verbose_name = "Título")
    subtitle = models.TextField(verbose_name = "Subitulo")
    image = models.ImageField( verbose_name = "Imagén", upload_to="services")
    text = models.TextField(verbose_name="Informacion", null=True, blank=True)


    created = models.DateTimeField( auto_now_add=True,  verbose_name = "Fecha creacion")
    updated =  models.DateTimeField( auto_now =True,  verbose_name = "Fecha Actualización")

# Create your models here.

    class Meta:
            verbose_name = "Servicio"
            verbose_name_plural = "Servicios"
            ordering  = ['-created']
    
    def __str__(self):
        return self.title