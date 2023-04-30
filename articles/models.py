from django.db import models

# Create your models here.

class Articles(models.Model):
    titulo= models.CharField(max_length=60)
    subtitulo= models.CharField(max_length=100)
    contenido= models.CharField(max_length=5000)
    cat= models.CharField(max_length=15, default='')
    likes=models.IntegerField(default=0)
    vistas= models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.titulo}'
        
    
    
    