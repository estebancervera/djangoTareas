from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    content = models.TextField(verbose_name = "Contenido")

    created = models.DateTimeField( auto_now_add=True,  verbose_name = "Fecha de Creacion")
    updated =  models.DateTimeField( auto_now =True,  verbose_name = "Fecha de Actualización")
    
    class Meta:
            verbose_name = "Pagina"
            verbose_name_plural = "Paginas"
            ordering  = ['title']
    
    def __str__(self):
        return self.title
