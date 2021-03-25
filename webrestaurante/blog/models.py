from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
   
    created = models.DateTimeField( auto_now_add=True,  verbose_name = "Fecha de Creacion")
    updated =  models.DateTimeField( auto_now =True,  verbose_name = "Fecha de Actualización")

    
    class Meta:
            verbose_name = "Categoria"
            verbose_name_plural = "Categorias"
            ordering  = ['-created']
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
   
    content = models.TextField(verbose_name = "Contenido")
    image = models.ImageField( verbose_name = "Imagén", upload_to="blog", null=True, blank=True)
    published = models.DateTimeField(verbose_name="Fecha de Publicacion", default=now)

    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name='get_posts')

    created = models.DateTimeField( auto_now_add=True,  verbose_name = "Fecha de Creacion")
    updated =  models.DateTimeField( auto_now =True,  verbose_name = "Fecha de Actualización")

    
    class Meta:
            verbose_name = "Blog"
            verbose_name_plural = "Blogs"
            ordering  = ['-created']
    
    def __str__(self):
        return self.title