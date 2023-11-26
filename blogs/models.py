from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    descripcion = models.TextField()
    fecha_creado = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    categorias = models.ManyToManyField('Categorias')
    destacado = models.BooleanField(default=False)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    pub_date = models.DateTimeField(default=timezone.now())
    
    def get_absolute_url(self):
        return reverse("blogs:post", kwargs={"slug": self.slug})
    
    class Meta:
        ordering = ["-fecha_creado"]
    
    
    def __str__(self):
        return self.titulo
    
class Categorias(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    
    def get_absolute_url(self):
        return reverse("blogs:categorias", kwargs={"slug": self.slug})
    
    
    def __str__(self):
        return self.titulo
    
class Comment(models.Model):
    content = models.TextField(max_length=1000, help_text='Ingrese un comentario')
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-post_date']

    def __str__(self):
        len_title = 15
        if len(self.content) > len_title:
            return self.content[:len_title] + '...'
        return self.content