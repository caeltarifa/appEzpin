from django.db import models
from datetime import datetime

# Create your models here.


class Usuario_ezpin(models.Model):
    designador=models.CharField(primary_key=True,max_length=8)
    descripcion=models.CharField(max_length=85)
    def __str__(self):
        return '{}'.format(self.designador)
    class Meta:
        ordering = ['designador']

class Grupo_ezpin(models.Model):
    predeterminado=models.CharField(primary_key=True,max_length=8)
    nombre_grupo=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=85)
    integrantes=models.ManyToManyField(Usuario_ezpin)
    def __str__(self):
        return '{}'.format(self.predeterminado)
    class Meta:
        ordering = ['predeterminado']


class Air_mensaje(models.Model):
    id_airmensaje = models.AutoField(primary_key=True)
    
    asunto=models.CharField(max_length=200)

    mensaje=models.TextField()

    visto=models.BooleanField(default=False)
    

    grupo_destino = models.ManyToManyField(Grupo_ezpin, blank=False)

    direccion_destino = models.ManyToManyField(Usuario_ezpin, blank=False)
    
    hora_enviado=models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.id_airmensaje, self.mensaje )
    class Meta:
        ordering = ['-id_airmensaje']
